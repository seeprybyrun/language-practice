import random
import copy
import csv

def permute(iterable):
    n = len(iterable)
    for i in range(n-1):
        j = random.randint(0,n-i-1)
        iterable[i], iterable[i+j] = iterable[i+j], iterable[i]
    return iterable

def choose_random_elements(iterable, num_to_choose):
    permuted_iterable = permute(copy.copy(iterable))
    return permuted_iterable[:num_to_choose]

print choose_random_elements(range(10),5)

