from collections import defaultdict

from lib import *
problem = old_aoc.Problem("2015/03: Perfectly Spherical Houses in a Vacuum")
problem.preprocessor = ppr.identity

@problem.solver(part=1)
def part1(inp):
    points = defaultdict(int)

    x, y = 0, 0

    points[(x, y)] += 1

    for move in inp:
        if move == "^":
            y += 1
        if move == "v":
            y -= 1
        if move == ">":
            x += 1
        if move == "<":
            x -= 1
        points[(x, y)] += 1
    
    return len(points)

@problem.solver(part=2)
def part2(inp):
    points = defaultdict(int)

    x, y = 0, 0
    rx, ry = 0, 0

    points[(x, y)] += 2

    for move in inp[::2]:
        if move == "^":
            y += 1
        if move == "v":
            y -= 1
        if move == ">":
            x += 1
        if move == "<":
            x -= 1
        points[(x, y)] += 1

    for move in inp[1::2]:
        if move == "^":
            ry += 1
        if move == "v":
            ry -= 1
        if move == ">":
            rx += 1
        if move == "<":
            rx -= 1
        points[(rx, ry)] += 1

    return len(points)

SAMPLE_INP =\
"""^v^v^v^v^v
"""

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 2, 11)