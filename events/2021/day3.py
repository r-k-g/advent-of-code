import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache, reduce
from copy import deepcopy

def constant_factory(value):
    return lambda: value

from lib import *
problem = aoc.Problem("2015/01: ???")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(inp):
    p1, p2 = 0, 0

    for v in inp:
        print(v)

    return (p1, p2)

SAMPLE_INP =\
"""
"""

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 0, 0)