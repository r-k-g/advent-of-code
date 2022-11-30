from lib import *
helper = aoc.Helper("2021/01", "???")

SAMPLE = """

"""
helper.check_sample(SAMPLE, 0, 0)

inp = helper.get_input().strip()
inp = inp.split("\n")

for l in inp:
    print(l)

print("Part 1:", 0)

# print("Part 2:", 0)