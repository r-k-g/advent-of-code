from collections import deque
from copy import deepcopy
import re

from lib import *
helper = aoc.Helper("2022/05", "Supply Stacks")

SAMPLE = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
helper.check_sample(SAMPLE, "CMZ", "MCD")

inp = helper.get_input().rstrip()
start, moves = [group.split("\n") for group in inp.split("\n\n")]

stacks = {int(i):deque() for i in start.pop(-1).split()}

for l in start:
    for i in range(len(l)):
        if l[i].isalpha():
            stacks[i//4 + 1].appendleft(l[i])

stacks2 = deepcopy(stacks)

for cmd in moves:
    amount, start, to = map(int, 
        re.match("move (\d+) from (\d+) to (\d+)", cmd).groups()
    )
    
    move1, move2 = [], []
    for _ in range(amount):
        move1.append(stacks[start].pop())
        move2.append(stacks2[start].pop())
    
    stacks[to].extend(move1)
    stacks2[to].extend(move2[::-1])

part1 = "".join(stacks[stack][-1] for stack in stacks)
part2 = "".join(stacks2[stack][-1] for stack in stacks2)

print("Part 1:", part1)
print("Part 2:", part2)