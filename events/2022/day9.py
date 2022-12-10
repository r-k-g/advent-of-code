import math
from lib import *
helper = aoc.Helper("2022/09", "Rope Bridge")

SAMPLE = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
helper.check_sample(SAMPLE, 88, 36)

inp = helper.get_input().strip().split("\n")

def touching(head, tail):
    return abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2

def sign(n):
    return (n > 0) - (n < 0)

movemap = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (1, 0),
    "R": (-1, 0),
}

knots = tuple([0, 0] for _ in range(10))

positions_1 = {(0, 0)}
positions_9 = {(0, 0)}

for move in inp:
    move, amount = move.split()
    move = movemap[move]

    for _ in range(int(amount)):
        knots[0][0] += move[0]
        knots[0][1] += move[1]
        
        for n in range(1, len(knots)):
            follow = knots[n-1]
            tail = knots[n]
            
            while not touching(follow, tail):
                tail[0] += sign(follow[0] - tail[0])
                tail[1] += sign(follow[1] - tail[1])
                
                positions_1.add(tuple(knots[1]))
                positions_9.add(tuple(knots[-1]))

print("Part 1:", len(positions_1))
print("Part 2:", len(positions_9))