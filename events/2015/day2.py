from itertools import combinations

from lib import *
problem = aoc.Problem("2015/02: I Was Told There Would Be No Math")
problem.preprocessor = lambda boxes: [
    [int(d) for d in box.split("x")] for box in boxes.strip().split("\n")
]

@problem.solver()
def solve(boxes):
    p1, p2 = 0, 0

    for b in boxes:
        sides = list(combinations(b, 2))
        for s in sides:
            p1 += 2 * s[0] * s[1]
        smallest = min(sides, key=lambda i: i[0] * i[1])
        p1 += smallest[0] * smallest[1]

        p2 += (smallest[0] * 2) + (smallest[1] * 2)
        p2 += b[0] * b[1] * b[2]

    return (p1, p2)

SAMPLE_INP =\
"""2x3x4
"""

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 58, 34)