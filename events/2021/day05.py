import re
from collections import defaultdict

from lib import *
problem = aoc.Problem("2021/05: Hydrothermal Venture")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(inp):
    linepoints1 = defaultdict(int)
    linepoints2 = defaultdict(int)

    for v in inp:
        m = re.match("(\d+),(\d+) -> (\d+),(\d+)", v)
        x1, y1, x2, y2 = map(int, m.groups())
        
        if x1 < x2:
            xrange = range(x1, x2 + 1)
        elif x1 > x2:
            xrange = range(x1, x2-1, -1)
        if y1 < y2:
            yrange = range(y1, y2 + 1)
        elif y1 > y2:
            yrange = range(y1, y2-1, -1)

        if x1 == x2:
            for y in yrange:
                linepoints1[(x1, y)] += 1
                linepoints2[(x1, y)] += 1
        elif y1 == y2:
            for x in xrange:
                linepoints1[(x, y1)] += 1
                linepoints2[(x, y1)] += 1
        else:
            for x, y in zip(xrange, yrange) :
                linepoints2[(x, y)] += 1

    p1 = len([i for i in linepoints1 if linepoints1[i] > 1])
    p2 = len([i for i in linepoints2 if linepoints2[i] > 1])

    return (p1, p2)

SAMPLE_INP = ("""
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 5, 12)