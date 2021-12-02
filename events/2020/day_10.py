import random, os, sys, re, statistics, itertools
from collections import deque, OrderedDict, Counter, defaultdict
from functools import lru_cache, reduce

from lib import *

problem = aoc.Problem("2020/10: Adapter Array")
problem.preprocessor = ppr.lsi

@problem.solver(part=1)
def part1(inp):
    joltages = sorted(inp)
    device = joltages[-1] + 3
    joltages = [0] + joltages + [device]

    diff1 = diff3 = 0
    for i, joltage in enumerate(joltages):
        if i == len(joltages)-1:
            break
        if joltages[i+1]-joltage == 1:
            diff1 += 1
        if joltages[i+1]-joltage == 3:
            diff3 += 1

    return  diff1 * diff3

@problem.solver(part=2)
def part2(inp):
    joltages = sorted(inp)
    device = joltages[-1] + 3

    dp = dict()
    dp[0] = 1
    for joltage in joltages + [device]:
        dp[joltage] = sum(dp.get(joltage-i, 0) for i in range(1, 4))
    return dp[joltage]


if __name__ == "__main__":
    problem.solve()
