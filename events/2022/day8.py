from lib import *
helper = aoc.Helper("2022/08", "???")

SAMPLE = """
30373
25512
65332
33549
35390
"""
helper.check_sample(SAMPLE, 21, 8)

inp = helper.get_input().strip()
trees = ppr.igrid(inp)

def check_up(x, y, dist=False):
    col = get_col(trees, x)
    start = trees[y][x]
    c = 1

    for c, y in enumerate(range(y-1, -1, -1), start=1):
        if col[y] < start:
            continue
        else:
            return c if dist else False

    return c if dist else True

def check_down(x, y, dist=False):
    col = get_col(trees, x)
    start = trees[y][x]
    c = 1

    for c, y in enumerate(range(y+1, len(trees)), start=1):
        if col[y] < start:
            continue
        else:
            return c if dist else False

    return c if dist else True

def check_right(x, y, dist=False):
    row = get_row(trees, y)
    start = trees[y][x]
    c = 1

    for c, i in enumerate(range(x+1, len(trees[0])), start=1):
        if row[i] < start:
            continue
        else:
            return c if dist else False

    return c if dist else True

def check_left(x, y, dist=False):
    row = get_row(trees, y)
    start = trees[y][x]
    c = 1

    for c, x in enumerate(range(x-1, -1, -1), start=1):
        if row[x] < start:
            continue
        else:
            return c if dist else False

    return c if dist else True

def is_visible(x, y):
    return any(
        func(x, y) for func in 
        [check_up, check_down, check_left, check_right]
    )

def get_score(x, y):
    if 0 in (x, y) or x == len(trees[0]) - 1 or y == len(trees) -1:
        return 0

    l = [
        func(x, y, dist=True) for func in 
        (check_up, check_down, check_left, check_right)
    ]
    return l[0] * l[1] * l[2] * l[3]

if helper.args.testing:
    pass

visible = set()
highest = 0

for x in range(len(trees[0])):
    for y in range(len(trees)):
        if is_visible(x, y):
            visible.add((x, y))
        highest = max(highest, get_score(x, y))
        if get_score(x, y) == 16 and helper.args.testing:
            print(x, y)

print("Part 1:", len(visible))
print("Part 2:", highest)