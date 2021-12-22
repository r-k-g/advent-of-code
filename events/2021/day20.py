from lib import *
problem = old_aoc.Problem("2021/20: Trench Map")
problem.preprocessor = ppr.llsv

@problem.solver()
def solve(inp):
    algo, img = inp
    algo = algo.replace(".", "0").replace("#", "1")
    img = [
        i.replace(".", "0").replace("#", "1")
        for i in img.split("\n")
    ]

    img = {
        (x, y): img[y][x] 
        for y in range(len(img)) 
        for x in range(len(img[y]))
    }

    return (simulate(img, algo, 2), simulate(img, algo, 50))

def simulate(img, algo, times):
    default = "0"
    img = img.copy()
    for i in range(times):
        new_img = {}
        xvals, yvals = zip(*img)
        for cy in range(min(yvals) - 1, max(yvals) + 2):
            for cx in range(min(xvals) - 1, max(xvals) + 2):
                group = ""
                for x, y in square_around(cx, cy):
                    group += img.get((x, y), default)
                num = int(group, 2)
                new_img[(x, y)] = algo[num]
        img = new_img

        if algo[0] == "1":
            default = "0" if i % 2 else "1"
    
    return count_on(img)

def count_on(img):
    c = 0
    for k in img:
        if img[k] == "1":
            c += 1
    return c

def square_around(x, y):
    deltas = (
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (0, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1),
    )
    coords = []
    for dx, dy in deltas:
        adj_x, adj_y = x + dx, y + dy
        coords.append((adj_x, adj_y))
    
    return coords

SAMPLE_INP = ("""
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 35, 3351)