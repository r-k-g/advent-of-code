import math
from lib import *
helper = aoc.Helper("2022/08", "Treetop Tree House")

SAMPLE = """
30373
25512
65332
33549
35390
"""
helper.check_sample(SAMPLE, 21, 8)

inp = helper.get_input().strip()
trees = ppr.igrid(inp)

def check(x, y, direction, dist=False):
    start = trees[y][x]
    c = 1

    if direction in ("up", "down"):
        group = get_col(trees, x)
    else:
        group = get_row(trees, y)
    
    indices = {
        "up": range(y-1, -1, -1),
        "down": range(y+1, len(trees)),
        "left": range(x-1, -1, -1),
        "right": range(x+1, len(trees[0])),
    }[direction]

    for c, i in enumerate(indices, start=1):
        if group[i] < start:
            continue
        else:
            return (False, c)

    return (True, c)

visible = set()
highest = 0

for x in range(len(trees[0])):
    for y in range(len(trees)):
        visibles, dists = zip(*[
            check(x, y, direction) 
            for direction in ("up", "down", "left", "right")
        ])

        if any(visibles):
            visible.add((x, y))

        if 0 not in (x, y, x+1 - len(trees[0]), y+1 - len(trees)):
            highest = max(highest, math.prod(dists))

print("Part 1:", len(visible))
print("Part 2:", highest)