import re

from lib import *
problem = old_aoc.Problem("2015/06: Probably a Fire Hazard")
problem.preprocessor = ppr.lsv

@problem.solver(part=1)
def part1(inp):
    lights = [[0] * 1000 for i in range(1000)]

    for v in inp:
        m = re.match("^([\w ]+) (\d+),(\d+) through (\d+),(\d+)", v)
        command, *numbers = m.groups()
        x1, y1, x2, y2 = map(int, numbers)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if command == "turn off":
                    lights[y][x] = 0
                elif command == "turn on":
                    lights[y][x] = 1
                elif command == "toggle":
                    lights[y][x] = int(not lights[y][x])

    p1 = sum(
        sum(row) for row in lights
    )

    return p1

@problem.solver(part=2)
def part2(inp):
    lights = [[0] * 1000 for i in range(1000)]

    for v in inp:
        m = re.match("^([\w ]+) (\d+),(\d+) through (\d+),(\d+)", v)
        command, *numbers = m.groups()
        x1, y1, x2, y2 = map(int, numbers)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if command == "turn off":
                    lights[y][x] = max(lights[y][x] - 1, 0)
                elif command == "turn on":
                    lights[y][x] += 1
                elif command == "toggle":
                    lights[y][x] +=  2

    p2 = sum(
        sum(row) for row in lights
    )

    return p2

if __name__ == "__main__":
    problem.solve("toggle 0,0 through 999,0", 1000, 2000)