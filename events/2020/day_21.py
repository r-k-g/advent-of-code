import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache, reduce
from copy import deepcopy

def constant_factory(value):
    return lambda: value

with open('day_21_inp.txt', 'r') as inp:
    result = ''.join(inp.read().split('\n')).split(')')
result = [g.split('(contains ') for g in result]
foods = [[i[0].split(), i[1].split(', ')] for i in result]

allingredients = list()
for i in foods:
    allingredients.extend(i[0])

ingredients = defaultdict(list)

for f in foods:
    for i in f[1]:
        ingredients[i].append(f[0])

for i in ingredients:
    ingredients[i] = list(set(ingredients[i][0]).intersection(*ingredients[i]))

print(ingredients)
items = list(ingredients.items())

while True:
    for i in items:
        if len(i[1]) == 1:
            for x in items:
                if x != i:
                    try:
                        x[1].remove(i[1][0])
                    except ValueError:
                        pass
    for i in items:
        if len(i[1]) > 1:
            break
    else:
        break

items.sort(key=lambda x: x[0])

print(','.join([i[1][0] for i in items]))