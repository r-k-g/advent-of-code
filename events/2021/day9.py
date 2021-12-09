from lib import *
problem = aoc.Problem("2021/09: Smoke Basin")
problem.preprocessor = lambda s: [
    [int(i) for i in l] for l in s.strip().split("\n")
]

@problem.solver()
def solve(inp):
    low_points = 0

    sizes = []

    for y, row in enumerate(inp):
        for x, val in enumerate(row):
            if all([val < adj for adj in get_adjacent(x, y, inp)]):
                low_points += val + 1
                sizes.append(basin_size(x, y, inp))

    sizes.sort(reverse=True)
    p2 = sizes[0] * sizes[1] * sizes[2]

    return (low_points, p2)

def basin_size(x, y, grid):
    size = 0
    
    queue = [(x, y)]
    visited = set()

    while queue:
        x, y = queue.pop(0)
        val = grid[y][x]

        if val == 9 or (x, y) in visited:
            continue

        visited.add((x, y))
        size += 1

        for adj_x, adj_y in get_adjacent(x, y, grid, coords=True):
            queue.append((adj_x, adj_y))

    return size

def get_adjacent(x, y, grid, coords=False):
    points = []
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for delta in deltas:
        adj_x, adj_y = x + delta[0], y + delta[1]
        if adj_x < 0 or adj_x >= len(grid[y]):
            continue
        if adj_y < 0 or adj_y >= len(grid):
            continue
        
        if coords:
            points.append((adj_x, adj_y))
        else:
            points.append(grid[adj_y][adj_x])
    
    return points


SAMPLE_INP =\
"""2199943210
3987894921
9856789892
8767896789
9899965678
"""

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 15, 1134)