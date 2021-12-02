from collections import defaultdict, Counter, deque
import itertools as it
import random
import re
import sys
import time

def part1(points):
    overlapping = 0
    for p in points:
        if len(points[p]) >= 2:
            overlapping += 1
    return overlapping


def part2(points):
    eligible = set()
    for p in points:
        if len(points[p]) == 1:
            for i in points[p]: # get item in set
                break
            eligible.add(i)

    for p in points:
        if len(points[p]) > 1:
            for i in points[p]:
                eligible.discard(i)

    return eligible

def main():
    with open("day3_inp.txt") as f:
        contents = f.read()

    points = dict()  # (x, y): [regionids]
    for l in contents.split("\n"):
        m = re.match("^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$", l)
        p_id, x, y, w, h = [int(m.group(i)) for i in range(1, 6)]
        
        for row in range(y, y+h):
            for col in range(x, x+w):
                if (col, row) in points:
                    points[(col, row)].add(p_id)
                else:
                    points[(col, row)] = {p_id}

    print(f"Part 1: {part1(points)}")
    print(f"Part 2: {part2(points)}")

if __name__ == "__main__":
    main()