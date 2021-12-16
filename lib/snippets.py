import heapq
from collections import defaultdict
from copy import deepcopy

UP = NORTH = (0, 1)
DOWN = SOUTH = (0, -1)
RIGHT = EAST = (1, 0)
LEFT = WEST = (-1, 0)

DIRECTIONS = {
    "up": UP,
    "down": DOWN,
    "left": LEFT,
    "right": RIGHT,
}
CARDINAL_DIRECTIONS = {
    "N": NORTH,
    "S": SOUTH,
    "E": EAST,
    "W": WEST
}

def nwise(iterable, n):
    """Return a generator of n-length sliding window over iterable."""
    iters = [iter(iterable) for i in range(n)]
    for i in range(n):
        for rep in range(i):
            next(iters[i])
    return zip(*iters)

def coords_around(x, y, direct=True, diagonal=True, 
                  validator=None, limits_grid=None):
    """Get the coordinates immediately around an (x, y) point."""
    
    if validator is None:
        if limits_grid is not None:
            validator = lambda a_x, a_y: all([
                a_x >= 0, a_y >= 0, 
                a_x < len(limits_grid[y]),
                a_y < len(limits_grid),
            ])
        else:
            validator = lambda *_: True
    
    deltas = (
        [(0, 1), (0, -1), (1, 0), (-1, 0)] * direct +
        [(-1, 1), (1, 1), (-1, -1), (1, -1)] * diagonal
    )
    for dx, dy in deltas:
        adj_x, adj_y = x + dx, y + dy
        if validator(adj_x, adj_y):
            yield (adj_x, adj_y)

def rotate_matrix(matrix, ccw=False):
    """Rotate a matrix by 90 degrees."""
    if ccw:
        return [list(i)[::-1] for i in zip(*matrix[::-1])][::-1]
    return [list(i) for i in zip(*matrix[::-1])]

def get_col(grid, col):
    """Get specified column from a grid."""
    return [row[col] for row in grid]

def get_row(grid, row, copy=True):
    """Get specified row from a grid, copy by default."""
    if copy:
        return grid[row].copy()
    return grid[row]

def flip_horizontal(grid):
    """Return a grid flipped horizontally."""
    new = []
    for row in grid:
        new.append(row[::-1])
    return new

def flip_vertical(grid):
    """Return a copy of a grid flipped verically."""
    return deepcopy(grid[::-1])

class WGraph:
    def __init__(self, nodes=None, edges=None):
        self.edges = defaultdict(dict) if edges is None else edges
        self.nodes = set(self.edges.keys()) if nodes is None else nodes
    
    def add_edge(self, node1, node2, weight, two_way=True):
        self.edges[node1][node2] = weight
        if two_way:
            self.edges[node2][node1] = weight
        
        self.nodes.add(node1)
        self.nodes.add(node2)
    
    def distances_from(self, start):
        distances = defaultdict(lambda: float("inf"))
        distances[start] = 0
        queue = [(0, start)]
        visited = set([start])

        while queue:
            cdist, current = heapq.heappop(queue)

            for node, dist in self.edges[current].items():
                distances[node] = min(
                    distances[node], 
                    cdist + dist
                )

                if node not in visited:
                    heapq.heappush(queue, (distances[node], node))
                    visited.add(node)
        
        return distances


