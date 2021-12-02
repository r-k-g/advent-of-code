from collections import defaultdict, Counter, deque
import itertools as it
import random
import sys
import time

def part1(inp):
    twos = 0
    threes = 0

    for line in inp:
        counts = Counter(line).values()
        if 2 in counts:
            twos += 1
        if 3 in counts:
            threes += 1

    return twos * threes

def remove_unique(s1, s2):
    res = []
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            continue
        res.append(c1)
    return "".join(res)

def part2(inp):
    enum = list(enumerate(inp))
    for i, line in enum:
        for x, rep in enum:
            if x == i:
                continue

            diff = 0
            for c1, c2 in zip(line, rep):
                if c1 != c2:
                    diff += 1
                if diff > 1:
                    break

            if diff == 1:
                return remove_unique(line, rep)


def main():
    with open("day2_inp.txt") as f:
        contents = f.read()

    inp = contents.split("\n")
    
    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")

if __name__ == "__main__":
    main()