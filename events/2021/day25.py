from lib import *
import sys
import itertools
helper = aoc.Helper("2021/25", "???")

SAMPLE = """
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""
helper.check_sample(SAMPLE, 58, "No part 2!")

inp = helper.get_input().strip()
grid = [list(l) for l in inp.split("\n")]

D = {
    ">": (1, 0),
    "v": (0, 1),
}

def pprint(grid):
    for l in grid:
        print("".join(l))

def do_step(grid, herdtype):
    newgrid = [["." for _ in range(len(grid[0]))] for i in range(len(grid))]

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            item = grid[y][x]
            
            if item not in herdtype:
                if item != ".":
                    newgrid[y][x] = item
                continue

            new_x = (x + D[item][0]) % len(grid[y])
            new_y = (y + D[item][1]) % len(grid)

            if grid[new_y][new_x] == ".":
                newgrid[new_y][new_x] = item
            else:
                newgrid[y][x] = item
    
    return newgrid

def tuplify(grid):
    return tuple("".join(l) for l in grid)

# if helper.args.testing:
states = set()
states.add(tuplify(grid))

for i in itertools.count(1):
    
    grid = do_step(grid, ">")
    grid = do_step(grid, "v")
    
    tuplified = tuplify(grid)
    # print(f"{states=}")
    if tuplified in states:
        break
    states.add(tuplified)


print("Part 1:", i)

print("Part 2:", "No part 2!")