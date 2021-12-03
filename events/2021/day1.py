import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache, reduce
from copy import deepcopy
from day2 import SAMPLE_INP

def constant_factory(value):
    return lambda: value

from lib import *
problem = aoc.Problem("2021/01: Sonar Sweep")
problem.preprocessor = ppr.lsi

@problem.solver()
def solve(inp):
    p1, p2 = -1, -1 # don't get off by one'd

    lastv = 0
    for v in inp:
        if v > lastv:
            p1 += 1
        lastv = v

    lastv = 0
    for n1, n2, n3 in zip(inp, inp[1:], inp[2:]):
        sum3 = n1 + n2 + n3
        if sum3 > lastv:
            p2 += 1
        lastv = sum3

    return (p1, p2)

SAMPLE_INP =\
"""199
200
208
210
200
207
240
269
260
263
"""

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 7, 5)