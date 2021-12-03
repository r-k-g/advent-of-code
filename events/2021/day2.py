from lib import *
problem = aoc.Problem("2021/02: Dive!")
problem.preprocessor = ppr.lsv

@problem.solver(part=1)
def part1(inp):
    x, y = 0, 0

    d = {"forward": (1, 0), "down": (0, 1), "up": (0, -1)}

    for v in inp:
        move, n = v.split()
        n = int(n)
        x += d[move][0] * n
        y += d[move][1] * n

    return x * y

@problem.solver(part=2)
def part2(inp):
    x, y = 0, 0
    aim = 0

    for v in inp:
        # print(v)
        move, n = v.split()
        n = int(n)

        if move == "down":
            aim += n
        elif move == "up":
            aim -= n
        elif move == "forward":
            x += n
            y += aim * n

    return x * y

SAMPLE_INP =\
"""forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 150, 900)