from lib import *
helper = aoc.Helper("2022/01", "Calorie Counting")

SAMPLE = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
helper.check_sample(SAMPLE, 24000, 45000)

inp = helper.get_input().strip()
elves = [sum(map(int, elf.split("\n"))) for elf in inp.split("\n\n")]

elves.sort(reverse=True)

print("Part 1:", elves[0])
print("Part 2:", sum(elves[0:3]))