from copy import deepcopy

from lib import *
problem = old_aoc.Problem("2021/13: Transparent Origami")
problem.preprocessor = lambda inp: inp.strip().split("\n\n")

@problem.solver()
def solve(inp):
    p1, p2 = 0, 0

    points, folds = inp[0], inp[1]
    points = [[int(i) for i in g.split(",")] for g in points.split("\n")]
    folds = folds.split("\n")


    debug = len(points) < 100

    xes, yes = [], []
    for x, y in points:
        xes.append(x)
        yes.append(y)
    xmax = max(xes)
    ymax = max(yes)
    
    grid = [["."] * (xmax + 1) for i in range(ymax + 1)]

    for x, y in points:
        grid[y][x] = "#"

    while folds:
        instr = folds.pop(0)
        if "x" in instr:
            _, xval = instr.split("=")
            xval = int(xval)

            left, right = partition(grid, split_x=xval)
            right = flip_horizontal(right)

            mainp = left if len(left[0]) > len(right[0]) else right
            other = left if mainp == right else right

            otherstart = len(mainp[0]) - len(other[0])

            new = deepcopy(mainp)
            for y in range(len(mainp)):
                for x in range(len(other[y])):
                    if "#" in (mainp[y][x+otherstart], other[y][x]):
                        new[y][x+otherstart] = "#"
                    else:
                        new[y][x+otherstart] = "."
            grid = new
        
        elif "y" in instr:
            _, yval = instr.split("=")
            yval = int(yval)

            upper, lower = partition(grid, split_y=yval)
            lower = flip_vert(lower)

            mainp = upper if len(upper) > len(lower) else lower
            other = upper if mainp == lower else lower

            otherstart = len(mainp) - len(other)
            

            new = deepcopy(mainp)
            for y in range(len(other)):
                for x in range(len(mainp[y])):
                    if "#" in (mainp[y+otherstart][x], other[y][x]):
                        new[y+otherstart][x] = "#"
                    else:
                        new[y+otherstart][x] = "."
            grid = new
    
    grid = new
    c = 0

    printgrid(grid)

    for row in grid:
        for i in row:
            if i == "#":
                c += 1
    print(c)

    return (p1, p2)

def printgrid(grid):
    for row in grid:
        print(row)

def flip_horizontal(grid):
    new = []
    for row in grid:
        new.append(row[::-1])
    return new

def flip_vert(grid):
    return deepcopy(grid[::-1])

def partition(grid, split_x=None, split_y=None):
    if split_x is not None:
        left = []
        right = []
        for y in range(len(grid)):
            leftrow = []
            rightrow = []
            for x in range(len(grid[y])):
                if x < split_x:
                    leftrow.append(grid[y][x])
                if x > split_x:
                    rightrow.append(grid[y][x])
            left.append(leftrow)
            right.append(rightrow)
        return left, right
    
    elif split_y is not None:
        upper, lower = grid[:split_y], grid[split_y + 1:]
        
        return deepcopy(upper), deepcopy(lower)

        


SAMPLE_INP = ("""
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 0, 0)