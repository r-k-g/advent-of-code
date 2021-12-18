import sys

import aoc

helper = aoc.Helper("2021/32", "A Puzzle")

SAMPLE = "1"
helper.check_sample(SAMPLE)

IN = helper.get_input() or sys.stdin.read()

n = 1 * int(IN.strip())
print("Part 1:", n)
print("Part 2:", -n)