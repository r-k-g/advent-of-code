import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache, reduce
from copy import deepcopy

def constant_factory(value):
    return lambda: value

from lib import *
problem = aoc.Problem("2016/03: Squares With Three Sides")
problem.preprocessor = lambda tris: [
    [int(side) for side in tri.split()] for tri in tris.strip().split("\n")
]

@problem.solver(part=1)
def part1(inp):
    valid = 0

    for tri in inp:
        sides = sorted(tri)
        if sides[0] + sides[1] > sides[2]:
            valid += 1

    return valid

@problem.solver(part=2)
def part2(inp):
    valid = 0

    for i in range(2, len(inp), 3):
        for j in range(3):
            sides = sorted([inp[i][j], inp[i-1][j], inp[i-2][j]])
            if sides[0] + sides[1] > sides[2]:
                valid += 1
    
    return valid

if __name__ == "__main__":
    problem.solve()