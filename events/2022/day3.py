from functools import reduce
from lib import *
helper = aoc.Helper("2022/03", "Rucksack Reorganization")

SAMPLE = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
helper.check_sample(SAMPLE, 157, 70)

sacks = helper.get_input().strip().split("\n")

def get_priority(item):
    return ord(item) - (96 if item.islower() else 38)

sum_priorities = 0
for sack in sacks:
    left, right = sack[:len(sack)//2], sack[len(sack)//2:]
    common = set(left) & set(right)

    sum_priorities += get_priority(common.pop())

print("Part 1:", sum_priorities)


badge_priorities = 0
for i in range(0, len(sacks), 3):
    common = reduce(set.intersection, map(set, sacks[i:i+3]))
    badge_priorities += get_priority(common.pop())

print("Part 2:", badge_priorities)