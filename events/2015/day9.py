import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache, reduce
from copy import deepcopy

def constant_factory(value):
    return lambda: value

from lib import *
problem = aoc.Problem("2015/09: All in a Single Night")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(inp):
    debug = len(inp) < 10

    p1, p2 = 0, 0

    distances = defaultdict(dict)

    for v in inp:
        m = re.fullmatch("(\w+) to (\w+) = (\d+)", v)
        start, destination, dist = m.groups()
        dist = int(dist)
        distances[start][destination] = dist
        distances[destination][start] = dist
    
    seq_distances = []
    for seq in permutations(distances):
        dist = 0
        for i in range(1, len(seq)):
            dist += distances[seq[i-1]][seq[i]]
        seq_distances.append(dist)
    

    return (min(seq_distances), max(seq_distances))

SAMPLE_INP =\
"""London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 605, 982)