import math
from copy import deepcopy

from lib import *
problem = aoc.Problem("2021/15: Chiton")
problem.preprocessor = ppr.igrid

@problem.solver()
def solve(inp):
    return (lowest_risk(inp, 1), lowest_risk(inp, 5))

def lowest_risk(grid, expand):
    w = len(grid[0])
    h = len(grid)

    big_grid = []
    for y in range(h * expand):
        row = []
        for x in range(w * expand):
            val = grid[y % h][x % w] + (y // h) + (x // w)
            if val > 9:
                val = val - 9
            row.append(val)
        big_grid.append(row)
    
    graph = WGraph()
    for y in range(len(big_grid)):
        for x in range(len(big_grid[y])):
            for adj_x, adj_y in coords_around(x, y, diagonal=False, limits_grid=big_grid):
                graph.add_edge((x, y), (adj_x, adj_y), big_grid[adj_y][adj_x], two_way=False)

    return graph.distances_from((0, 0))[(len(big_grid[-1]) - 1, len(big_grid) - 1)]

SAMPLE_INP = ("""
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 40, 315)