import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache, reduce
from copy import deepcopy

class Name:
    def __init__(self, ):
        pass
    
    def func(self):
        pass

with open('day_16_inp.txt', 'r') as inp:
    result = inp.read()

result = [g.split('\n') for g in result.split('\n\n')]

rules = dict()
for r in result[0]:
    k, v = r.split(': ')

    v = v.split(' or ')
    v = [range(int(s.split('-')[0]), int(s.split('-')[1]) + 1) for s in v]
    rules[k] = v

field_ord = dict.fromkeys(rules.keys())
for k in field_ord:
    field_ord[k] = list(range(len(field_ord)))

other_ticks = result[2][1:]
other_ticks2 = other_ticks.copy()

invalids = list()

for t in range(len(other_ticks)):

    fields = [int(i) for i in other_ticks[t].split(',')]
    for f in fields:
        if any([1 for k in rules if (f in rules[k][0]) or (f in rules[k][1])]):
            continue
        else:
            invalids.append(f)
            other_ticks2[t] = 0
            break

other_ticks2 = [i for i in other_ticks2 if i != 0]

for t in range(len(other_ticks2)):
    fields = [int(i) for i in other_ticks2[t].split(',')]
    for f in range(len(fields)):
        for r in rules:
            if (fields[f] in rules[r][0]) or (fields[f] in rules[r][1]):
                continue
            else:
                field_ord[r].remove(f)
for i in range(len(field_ord)):
    for r in field_ord:
        if len(field_ord[r]) == 1:
            for x in field_ord:
                if x != r:
                    try:
                        field_ord[x].remove(field_ord[r][0])
                    except ValueError:
                        continue


print(field_ord)

self_tick = [int(i) for i in result[1][1:][0].split(',')]

d_inds = [field_ord[i][0] for i in field_ord if i.startswith('departure')]

print(reduce((lambda x, y: x * y), [self_tick[i] for i in d_inds]))