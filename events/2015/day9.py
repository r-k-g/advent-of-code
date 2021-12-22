import re
from collections import defaultdict
from itertools import permutations

from lib import *
problem = old_aoc.Problem("2015/09: All in a Single Night")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(inp):
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