from itertools import product

from lib import *
problem = aoc.Problem("2021/11: Dumbo Octopus")
problem.preprocessor = lambda s: [
    [int(i) for i in l] for l in s.strip().split("\n")
]

@problem.solver()
def solve(grid):
    flashes, p2 = 0, 0

    step = 1
    while True:
        step_flashes = do_step(grid)
        if step <= 100:
            flashes += step_flashes
        
        if all([i == 0 for row in grid for i in row]):
            break
        step += 1

    return (flashes, step)

def print_grid(grid):
    for row in grid:
        print("".join(map(str, row)))

def do_step(grid):
    # increase by one
    for y, row in enumerate(grid):
        for x, octo in enumerate(row):
            grid[y][x] += 1

    flashed = set()
    to_flash = []
    for y, row in enumerate(grid):
        for x, octo in enumerate(row):
            if octo > 9 and (x, y) not in flashed:
                to_flash.append((x, y))
    
    while to_flash:
        x, y = to_flash.pop(0)

        for adj_x, adj_y in neighbours(x, y, grid):
            if (adj_x, adj_y) in flashed or (adj_x, adj_y) in to_flash:
                continue
            grid[adj_y][adj_x] += 1
            if grid[adj_y][adj_x] > 9:
                to_flash.append((adj_x, adj_y))

        flashed.add((x, y))
        
    for x, y in flashed:
        grid[y][x] = 0
    
    return len(flashed)

def neighbours(x, y, grid):
    deltas = product([-1, 0, 1], repeat=2)
    for delta in deltas:
        adj_x = x + delta[0]
        adj_y = y + delta[1]
        if adj_x < 0 or adj_y < 0:
            continue
        if adj_x > (len(grid[0]) - 1) or adj_y > (len(grid) - 1):
            continue
        if delta != (0, 0):
            yield adj_x, adj_y

SAMPLE_INP = ("""
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 1656, 195)