# -*- coding: utf-8 -*-

tense = "présent"
mood = "indicatif"

pronouns = ["je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles"]


er_verbs = ["adorer",
			"aimer",
			# "aimermieux",
			"allumer",
			"arriver",
			"apporter",
			"bavarder",
			"casser",
			"cesser",
			"chanter",
			"chercher",
			"créer",
			"danser",
			"déjeuner",
			"demander",
			"dépenser",
			"dessiner",
			"détester",
			"donner",
			"écouter",
			"emporter",
			"emprunter",
			"étudier",
			"fonder",
			"frapper",
			"gagner",
			"garder",
			"habiter",
			"jouver",
			"laisser",
			"montrer",
			"oublier",
			"parler",
			"pousser",
			"présenter",
			"prêter",
			"raconter",
			"recontrer",
			"regarder",
			"retrouver",
			"rester",
			"rouler",
			"saluer",
			"sauvegarder",
			"sauver",
			"supporter",
			"supprimer",
			"téléphoner",
			"terminer",
			"travailler",
			"traverser",
			"trouver",
			"voler",
			"aménager",
			"arranger",
			"changer",
			"corriger",
			"décourager",
			"déménager",
			"déranger",
			"diriger",
			"encourager",
			"engager",
			"loger",
			"manger",
			"nager",
			"partager",
			"plonger",
			"ranger",
			"rédiger",
			"télécharger",
			"voyager",
			"annoncer",
			"avancer",
			"commencer",
			"divorcer",
			"effacer",
			"lancer",
			"menacer",
			"placer",
			"prononcer",
			"renoncer",
			"replacer",
			"appuyer",
			"balayer",
			"effrayer",
			"employer",
			"ennuyer",
			"envoyer",
			"essayer",
			"essuyer",
			"nettoyer",
			"noyer",
			"payer",
			"rayer",
			"renvoyer",
			"tutoyer",
			"vouvoyer",
			"acheter",
			"amener",
			"emmener",
			"enlever",
			"geler",
			"lever",
			"mener",
			"peser",
			"promener",
			"appeler",
			"épeler",
			"feuilleter",
			"jeter",
			"projeter",
			"rappeler",
			"rejeter",
			"renouveler",
			"espérer",
			"préférer",
			"céder",
			"célébrer",
			"compléter",
			"protéger",
			"refléter",
			"répéter",
			"révéler",
			]

er_e_grave = {"acheter",
			  "amener",
			  "emmener",
			  "enlever",
			  "geler",
			  "lever",
			  "mener",
			  "peser",
			  "promener",
			 }

er_double_consonant = {"appeler",
					   "épeler",
					   "feuilleter",
					   "jeter",
					   "projeter",
					   "rappeler",
					   "rejeter",
					   "renouveler",
					  }

er_e_acute = {"espérer",
			  "préférer",
			  "céder",
			  "célébrer",
			  "compléter",
			  "protéger",
			  "refléter",
			  "répéter",
			  "révéler",
			  }

basic_er_conjugations = {"je": "e",
				   "tu": "es",
				   "il": "e",
				   "elle": "e",
				   "on": "e",
				   "nous": "ons",
				   "vous": "ez",
				   "ils": "ent",
				   "elles": "ent"}

er_ends_in_g_conjugations = {"nous": "geons"}

er_ends_in_c_conjugations = {"nous": "çons"}

er_ends_in_y_conjugations = {"je": "ie",
				   			 "tu": "ies",
				   			 "il": "ie",
				   			 "elle": "ie",
				   			 "on": "ie",
				   			 "ils": "ient",
				   			 "elles": "ient"}


ir_verbs = [
			]

basic_ir_conjugations = {"je": "is",
				   "tu": "is",
				   "il": "it",
				   "elle": "it",
				   "on": "it",
				   "nous": "issons",
				   "vous": "issez",
				   "ils": "issent",
				   "elles": "issent"}


irregular_verbs = {
	"aller": {
			"je": "vais",
			"tu": "vas",
			"il": "va",
			"elle": "va",
			"on": "va",
			"nous": "allons",
			"vous": "allez",
			"ils": "vont",
			"elles": "vont"
			},
	"apprendre": {
			"je": "apprends",
			"tu": "apprends",
			"il": "apprend",
			"elle": "apprend",
			"on": "apprend",
			"nous": "apprenons",
			"vous": "apprenez",
			"ils": "apprennent",
			"elles": "apprennent"
			},
	"avoir": {
			"je": "suis",
			"tu": "es",
			"il": "est",
			"elle": "est",
			"on": "est",
			"nous": "sommes",
			"vous": "êtes",
			"ils": "sont",
			"elles": "sont"
			},
	"comprendre": {
			"je": "comprends",
			"tu": "comprends",
			"il": "comprend",
			"elle": "comprend",
			"on": "comprend",
			"nous": "comprenons",
			"vous": "comprenez",
			"ils": "comprennent",
			"elles": "comprennent"
			},
	"devenir": {
			"je": "deviens",
			"tu": "deviens",
			"il": "devient",
			"elle": "devient",
			"on": "devient",
			"nous": "devenons",
			"vous": "devenez",
			"ils": "deviennent",
			"elles": "deviennent"
			},
	"devoir": {
			"je": "dois",
			"tu": "dois",
			"il": "doit",
			"elle": "doit",
			"on": "doit",
			"nous": "devons",
			"vous": "devez",
			"ils": "doivent",
			"elles": "doivent"
			},
	"dire": {
			"je": "dis",
			"tu": "dis",
			"il": "dit",
			"elle": "dit",
			"on": "dit",
			"nous": "disons",
			"vous": "dites",
			"ils": "disent",
			"elles": "disent"
			},
	"dormir": {
			"je": "dors",
			"tu": "dors",
			"il": "dort",
			"elle": "dort",
			"on": "dort",
			"nous": "dormons",
			"vous": "dormez",
			"ils": "dorment",
			"elles": "dorment"
			},
	"être": {
			"je": "suis",
			"tu": "es",
			"il": "est",
			"elle": "est",
			"on": "est",
			"nous": "sommes",
			"vous": "êtes",
			"ils": "sont",
			"elles": "sont"
			},
	"faire": {
			"je": "fais",
			"tu": "fais",
			"il": "fait",
			"elle": "fait",
			"on": "fait",
			"nous": "faisons",
			"vous": "faites",
			"ils": "font",
			"elles": "font"
			},
	"lire": {
			"je": "lis",
			"tu": "lis",
			"il": "lit",
			"elle": "lit",
			"on": "lit",
			"nous": "lisons",
			"vous": "lisez",
			"ils": "lisent",
			"elles": "lisent"
			},
	"maintenir": {
			"je": "maintiens",
			"tu": "maintiens",
			"il": "maintient",
			"elle": "maintient",
			"on": "maintient",
			"nous": "maintenons",
			"vous": "maintenez",
			"ils": "maintiennent",
			"elles": "maintiennent"
			},
	"partir": {
			"je": "pars",
			"tu": "pars",
			"il": "part",
			"elle": "part",
			"on": "part",
			"nous": "partons",
			"vous": "partez",
			"ils": "partent",
			"elles": "partent"
			},
	"pouvoir": {
			"je": "peux",
			"tu": "peux",
			"il": "peut",
			"elle": "peut",
			"on": "peut",
			"nous": "pouvons",
			"vous": "pouvez",
			"ils": "peuvent",
			"elles": "peuvent"
			},
	"prendre": {
			"je": "prends",
			"tu": "prends",
			"il": "prend",
			"elle": "prend",
			"on": "prend",
			"nous": "prenons",
			"vous": "prenez",
			"ils": "prennent",
			"elles": "prennent"
			},
	"retenir": {
			"je": "retiens",
			"tu": "retiens",
			"il": "retient",
			"elle": "retient",
			"on": "retient",
			"nous": "retenons",
			"vous": "retenez",
			"ils": "retiennent",
			"elles": "retiennent"
			},
	"revenir": {
			"je": "reviens",
			"tu": "reviens",
			"il": "revient",
			"elle": "revient",
			"on": "revient",
			"nous": "revenons",
			"vous": "revenez",
			"ils": "reviennent",
			"elles": "reviennent"
			},
	"savoir": {
			"je": "sais",
			"tu": "sais",
			"il": "sait",
			"elle": "sait",
			"on": "sait",
			"nous": "savons",
			"vous": "savez",
			"ils": "savent",
			"elles": "savent"
			},
	"sortir": {
			"je": "sors",
			"tu": "sors",
			"il": "sort",
			"elle": "sort",
			"on": "sort",
			"nous": "sortons",
			"vous": "sortez",
			"ils": "sortent",
			"elles": "sortent"
			},
	"surprendre": {
			"je": "surprends",
			"tu": "surprends",
			"il": "surprend",
			"elle": "surprend",
			"on": "surprend",
			"nous": "surprenons",
			"vous": "surprenez",
			"ils": "surprennent",
			"elles": "surprennent"
			},
	"tenir": {
			"je": "tiens",
			"tu": "tiens",
			"il": "tient",
			"elle": "tient",
			"on": "tient",
			"nous": "tenons",
			"vous": "tenez",
			"ils": "tiennent",
			"elles": "tiennent"
			},
	"venir": {
			"je": "viens",
			"tu": "viens",
			"il": "vient",
			"elle": "vient",
			"on": "vient",
			"nous": "venons",
			"vous": "venez",
			"ils": "viennent",
			"elles": "viennent"
			},
	"vouloir": {
			"je": "veux",
			"tu": "veux",
			"il": "veut",
			"elle": "veut",
			"on": "veut",
			"nous": "voulons",
			"vous": "voulez",
			"ils": "veulent",
			"elles": "veulent"
			},
}

for verb in er_verbs:

	for pronoun in pronouns:

		if verb in er_e_grave and pronoun not in ['nous','vous']:
			stem = verb[:-2]
			index_of_last_e = len(stem) - stem[::-1].find('e') - 1
			new_stem = stem[:index_of_last_e] + 'è' + stem[index_of_last_e+1:]
			new_verb = new_stem + 'er'
		elif verb in er_e_acute and pronoun not in ['nous','vous']:
			stem = verb[:-2].decode('utf-8')
			e_acute = 'é'.decode('utf-8')
			e_grave = 'è'.decode('utf-8')
			index_of_last_e = len(stem) - stem[::-1].find(e_acute) - 1
			new_stem = stem[:index_of_last_e] + e_grave + stem[index_of_last_e+1:]
			new_verb = (new_stem + 'er').encode('utf-8')
		elif verb in er_double_consonant and pronoun not in ['nous','vous']:
			new_stem = verb[:-2] + verb[-3]
			new_verb = new_stem + 'er'
		else:
			new_verb = verb

		if new_verb[-3:] == 'ger' and pronoun in er_ends_in_g_conjugations:
			conjugation = new_verb[:-3] + er_ends_in_g_conjugations[pronoun]
		elif new_verb[-3:] == 'cer' and pronoun in er_ends_in_c_conjugations:
			conjugation = new_verb[:-3] + er_ends_in_c_conjugations[pronoun]
		elif new_verb[-3:] == 'yer' and pronoun in er_ends_in_y_conjugations:
			conjugation = new_verb[:-3] + er_ends_in_y_conjugations[pronoun]
		else:
			conjugation = new_verb[:-2] + basic_er_conjugations[pronoun]

		print ','.join([verb, pronoun, mood, tense, conjugation])



for verb in irregular_verbs:
	for pronoun in pronouns:
		conjugation = irregular_verbs[verb][pronoun]
		print ','.join([verb, pronoun, mood, tense, conjugation])
