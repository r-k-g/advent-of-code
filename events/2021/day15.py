import math

from lib import *
problem = aoc.Problem("2021/15: Chiton")
problem.preprocessor = ppr.igrid

@problem.solver()
def solve(inp):
    return (lowest_risk(inp, 1), lowest_risk(inp, 5))

def lowest_risk(grid, expand):
    global dist_graph
    w = len(grid[0])
    h = len(grid)

    dist_graph = {}
    big_grid = []
    for y in range(h * expand):
        row = []
        for x in range(w * expand):
            dist_graph[(x, y)] = math.inf
            val = grid[y % h][x % w] + (y // h) + (x // w)
            if val > 9:
                val = val - 9
            row.append(val)
        big_grid.append(row)

    for y in range(len(big_grid)):
        for x in range(len(big_grid[y])):
            dist_graph[(x, y)] = path_risk_to((0, 0), (x, y), big_grid, set(), 0)
    
    return dist_graph[(len(big_grid[-1]) - 1, len(big_grid) - 1)] - big_grid[0][0]

all_lengths = set()
def path_risk_to(start, goal, grid, path, risk):
    risk += grid[start[1]][start[0]]
    path.add(start)

    validthings = []
    for x, y in coords_around(*goal, diagonal=False, limits_grid=grid):
        if (x, y) in dist_graph and dist_graph[(x, y)] != math.inf:
            validthings.append(dist_graph[(x, y)])
    if validthings:
        return min(validthings) + grid[goal[1]][goal[0]]

    if start == goal:
        return risk

SAMPLE_INP = ("""
11119
99919
91119
91999
91111
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 40, 315)