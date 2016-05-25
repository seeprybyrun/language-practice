# -*- coding: utf-8 -*-

import os
import random
import copy
import csv

import jinja2
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import memcache


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


this_quiz = dict()


# Knuth shuffle (adapted from Wikipedia entry on random permutations)
def permute(iterable):
    n = len(iterable)
    for i in range(n-1):
        j = random.randint(0,n-i-1)
        iterable[i], iterable[i+j] = iterable[i+j], iterable[i]
    return iterable


def choose_random_elements(iterable, num_to_choose):
    permuted_iterable = permute(copy.copy(iterable))
    return permuted_iterable[:num_to_choose]



# TODO: add user profiles, number attempts per question, number times correct, datetimes of most recent attempts

class EToFDefinitionQuestion(ndb.Model):
    english_glosses = ndb.StringProperty(required=True)
    french_answers = ndb.StringProperty(required=True)
    tags = ndb.StringProperty()


class ConjugationQuestion(ndb.Model):
    pronoun = ndb.StringProperty(required=True)
    verb_infinitive = ndb.StringProperty(required=True)
    tense = ndb.StringProperty(required=True)
    mood = ndb.StringProperty(required=True)
    correct_answer = ndb.StringProperty(required=True)
    tags = ndb.StringProperty() #for irregular verbs, -er verbs, -ir verbs, -re verbs, etc.



class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)


    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)


    def render(self, template, **kw):
        output = self.render_str(template, **kw)
        self.write(output.encode('utf-8'))


class MainPage(Handler):
    def get(self):
        self.redirect('/quiz-select')


class QuizSelect(Handler):
    def get(self):
        self.render('quiz-select.html')


    def post(self):
        # get random question keys to make the quiz
        quiz_type = self.request.get('quiz-type')
        num_quiz_questions = int(self.request.get('num-questions'))
        prompt = ''

        if quiz_type == "e2f-verb-definitions":
            all_question_keys = memcache.get('e2f_verb_definition_question_keys')
            if not all_question_keys:
                all_question_keys = EToFDefinitionQuestion.query().fetch(keys_only=True) # TODO: filter on type of definition
                memcache.set('e2f_verb_definition_question_keys', all_question_keys)

        if quiz_type == "e2f-all-definitions":
            all_question_keys = memcache.get('e2f_definition_question_keys')
            if not all_question_keys:
                all_question_keys = EToFDefinitionQuestion.query().fetch(keys_only=True)
                memcache.set('e2f_definition_question_keys', all_question_keys)

        elif quiz_type == "conjugation-indicative-present":
            all_question_keys = memcache.get('conjugation_question_keys')
            if not all_question_keys:
                all_question_keys = ConjugationQuestion.query().fetch(keys_only=True)
                memcache.set('conjugation_question_keys', all_question_keys)

        question_keys = choose_random_elements(all_question_keys, num_quiz_questions)

        this_quiz['quiz_type'] = quiz_type
        this_quiz['question_keys'] = question_keys
        this_quiz['question_number'] = 0
        this_quiz['num_correct'] = 0

        self.redirect('/quiz-question')


class QuizQuestion(Handler):
    def get(self):

        try:
            this_question_number = this_quiz['question_number']
            question_key = this_quiz['question_keys'][this_question_number]

            this_question = memcache.get(question_key.urlsafe())
            if not this_question:
                this_question = question_key.get()
                memcache.set(question_key.urlsafe(), this_question)

            kwd = dict()

            if this_quiz['quiz_type'] in ['e2f-all-definitions']:

                    kwd = {'english_glosses': this_question.english_glosses.encode('utf-8'),
                           'correct_answer': this_question.french_answers.encode('utf-8')}
                    prompt = "{english_glosses}".format(**kwd)

            elif this_quiz['quiz_type'] == 'conjugation-indicative-present':
                kwd = {'pronoun': this_question.pronoun.encode('utf-8'),
                       'verb_infinitive': this_question.verb_infinitive.encode('utf-8'),
                       'correct_answer': this_question.correct_answer.encode('utf-8')}
                prompt = "{pronoun} / {verb_infinitive}".format(**kwd)

            this_quiz['this_question_kwd'] = kwd
            this_quiz['this_question_prompt'] = prompt

            self.render('quiz-question.html', prompt=prompt.decode('utf-8'))
        except Exception as e:
            print "question_number: {}".format(this_question_number)
            key = this_quiz['question_keys'][this_question_number]
            print "key.id(): {}".format(key.id())
            raise e

    def post(self):
        go_to_next_question = (self.request.get('go-to-next-question') == 'yes')

        if go_to_next_question:
            this_quiz['question_number'] += 1

            if this_quiz['question_number'] < len(this_quiz['question_keys']):
                self.redirect('/quiz-question')
            else:
                self.redirect('/quiz-results')

        else:
            prompt = this_quiz['this_question_prompt']

            kwd = this_quiz['this_question_kwd']
            student_ans = self.request.get('student-answer')
            correct_ans = kwd['correct_answer'].split('|')

            feedback = 'Erreur'
            if student_ans.encode('utf-8') in correct_ans:
                feedback = 'Une bonne réponse!'
                this_quiz['num_correct'] += 1
            else:
                feedback = 'Désolé, l{pl0} bonne{pl1} réponse{pl1} {pl2} « {correct_answer} ».'
                feedback = feedback.format(pl0="a" if len(correct_ans) == 1 else "es",
                                           pl1="" if len(correct_ans) == 1 else "s",
                                           pl2="est" if len(correct_ans) == 1 else "sont",
                                           correct_answer=', '.join(correct_ans))

            self.render('quiz-answer.html', prompt=prompt.decode('utf-8'),
                filled_in_value=student_ans,
                feedback=feedback.decode('utf-8'))


class QuizResults(Handler):
    def get(self):
        num_correct = this_quiz['num_correct']
        num_attempted = this_quiz['question_number']
        plural_marker = 's' if num_correct != 1 else ''
        avoir_form = 'ont' if num_correct != 1 else 'a'

        feedback = "{} réponse{} sur {} {} été correcte{}.".format(num_correct,
            plural_marker, num_attempted, avoir_form, plural_marker)

        self.render('quiz-results.html', feedback=feedback.decode('utf-8'))

    def post(self):
        self.redirect('/quiz-select')


class AdminPage(Handler):
    def get(self):
        self.render('admin-page.html', response='')


    def post(self):
        task = self.request.get('task')
        response = 'No action performed.'

        if task == 'Clear Database':
            self.clear_e2f_definition_questions()
            self.clear_conjugation_questions()
            response = 'Database cleared.'

        elif task == 'Populate Database':
            self.populate_e2f_definition_questions()
            self.populate_conjugation_questions()
            response = 'Database populated.'

        self.render('admin-page.html', response=response)


    def populate_e2f_definition_questions(self):
        f = open('data/e2f_definition_questions.csv', 'r')
        reader = csv.reader(f, delimiter=';', quotechar='"')

        dqs = []

        for row in reader:
            if not row[0]:
                continue

            french_answers, english_glosses = row[0:2]
            tags = '|'.join(row[2:])
            dq = EToFDefinitionQuestion(french_answers=french_answers, english_glosses=english_glosses, tags=tags)
            dqs.append(dq)

        dq_keys = ndb.put_multi(dqs)
        memcache.set('e2f_definition_question_keys', dq_keys)

        f.close()


    def populate_conjugation_questions(self):
        f = open('data/conjugation_questions.csv', 'r')
        reader = csv.reader(f, delimiter=',', quotechar='"')

        cqs = []

        for row in reader:
            if not row[0]:
                continue

            verb_infinitive, pronoun, mood, tense, conjugation = row[0:5]
            cq = ConjugationQuestion(pronoun=pronoun, verb_infinitive=verb_infinitive,
                mood=mood, tense=tense, correct_answer=conjugation)
            cqs.append(cq)

        cq_keys = ndb.put_multi(cqs)
        memcache.set('conjugation_question_keys', cq_keys)

        f.close()


    def clear_e2f_definition_questions(self):
        dq_keys = EToFDefinitionQuestion.query().fetch(keys_only=True)
        if dq_keys:
            ndb.delete_multi(dq_keys)
        memcache.set('e2f_definition_question_keys', None)


    def clear_conjugation_questions(self):
        cq_keys = ConjugationQuestion.query().fetch(keys_only=True)
        if cq_keys:
            ndb.delete_multi(cq_keys)
        memcache.set('conjugation_question_keys', None)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/quiz-select', QuizSelect),
    ('/quiz-question', QuizQuestion),
    ('/quiz-results', QuizResults),
    ('/admin', AdminPage),
], debug=True)

