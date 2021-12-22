from collections import Counter

from lib import *
problem = old_aoc.Problem("2017/04: High-Entropy Passphrases")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(inp):
    p1, p2 = 0, 0

    for v in inp:
        if len(v.split()) == len(set(v.split())):
            p1 += 1
    
        v = v.split()
        v = ["".join(sorted(i)) for i in v]
        
        if Counter(v).most_common()[0][1] == 1:
            p2 += 1

    return (p1, p2)

SAMPLE_INP =\
"""
"""

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 0, 0)