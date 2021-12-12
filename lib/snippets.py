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
            validator = lambda _, _1: True
    
    deltas = (
        [(0, 1), (0, -1), (1, 0), (-1, 0)] * direct +
        [(-1, 1), (1, 1), (-1, -1), (1, -1)] * diagonal
    )
    for dx, dy in deltas:
        adj_x, adj_y = x + dx, y + dy
        if validator(adj_x, adj_y):
            yield (adj_x, adj_y)
