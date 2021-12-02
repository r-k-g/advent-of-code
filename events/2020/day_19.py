import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache
from copy import deepcopy

def constant_factory(value):
    return lambda: value

def check(rqueue, message):
    if not rqueue:
        return not message
    
    rule, *rqueue = rqueue
    rule = rules[rule]
    
    if isinstance(rule, str):
        try:
            return message[0] == rule and check(rqueue, message[1:])
        except IndexError:
            return False
    
    else:
        return any(check(option + rqueue, message) for option in rule)


with open('day_19_inp.txt', 'r') as inp:
    result = inp.read()

result = [g.split('\n') for g in result.split('\n\n')]

messages = result[1]

rules = defaultdict(list)

for r in result[0]:
    l = r.split(': ')
    if l[1][0].isnumeric():
        rules[int(l[0])].extend([[int(x) for x in si.split()] for si in l[1].split(' | ')])
    else:
        rules[int(l[0])] = l[1].replace('"', '')

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

valid = 0
for m in messages:
    if check([0], m):
        valid += 1

print(valid)