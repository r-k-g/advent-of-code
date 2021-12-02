import random, os, sys, re, statistics, time
from collections import deque, OrderedDict, Counter
from itertools import chain, combinations, permutations
from functools import lru_cache, reduce
from copy import deepcopy


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

with open('day_13_inp.txt', 'r') as inp:
    result = inp.read().split('\n')[1:]

busses = [int(b) if  b.isdigit() else b for b in ''.join(result).split(',') ]
print(busses)

n = list()
a = list()

for i, bus in enumerate(busses):
    if bus == 'x':
        continue
    
    n.append(bus)
    a.append(-i % bus)

print(chinese_remainder(n, a))