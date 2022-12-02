from lib import *
helper = aoc.Helper("2017/02", "Corruption Checksum")

SAMPLE = """
5 9 2 8
9 4 7 3
3 8 6 5
"""
helper.check_sample(SAMPLE, 18, 9)

inp = helper.get_input().strip()
rows = inp.split("\n")

grid = [[*map(int, row.split())] for row in rows]

total = 0
for r in grid:
    total += max(r) - min(r)

total2 = 0
for r in grid:
    for x in r:
        for y in r:
            # Inputs conveniently don't have duplicate values
            if y != x and y % x == 0:
                total2 += y//x

print("Part 1:", total)
print("Part 2:", total2)