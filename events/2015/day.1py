from lib import *
helper = aoc.Helper("2015/01", "Not Quite Lisp")

SAMPLE = """
()())
"""
helper.check_sample(SAMPLE, -1, 5)

inp = helper.get_input().strip()

print("Part 1:", inp.count("(") - inp.count(")"))

floor = 0
for i in range(len(inp)):
    if inp[i] == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        break

print("Part 2:", i + 1)