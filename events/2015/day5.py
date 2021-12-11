import re

from lib import *
problem = aoc.Problem("2015/05: Doesn't He Have Intern-Elves For This?")
problem.preprocessor = ppr.lsv

VOWELS = "aeiou"

@problem.solver()
def solve(inp):
    nice1, nice2 = 0, 0

    for string in inp:
        if is_nice1(string):
            nice1 += 1
        if is_nice2(string):
            nice2 += 1

    return (nice1, nice2)

def is_nice1(string):
    return (
        len([i for i in string if i in VOWELS]) >= 3
        and any([string[i] == string[i-1] for i in range(1, len(string))])
        and not any([sub in string for sub in ("ab", "cd", "pq", "xy")])
    )

def is_nice2(string):
    return (
        re.search(r"(..).*\1", string)
        and re.search(r"(.).\1", string)
    )

if __name__ == "__main__":
    problem.solve()