from lib import *
problem = aoc.Problem("2017/05: A Maze of Twisty Trampolines, All Alike")
problem.preprocessor = ppr.lsi

@problem.solver(part=1)
def part1(commands):
    position = 0
    steps = 0

    while 0 <= position < len(commands):
        
        jump = commands[position]
        commands[position] += 1
        position += jump

        steps += 1
        
    return steps

@problem.solver(part=2)
def part2(commands):
    position = 0
    steps = 0

    while 0 <= position < len(commands):
        
        jump = commands[position]

        if jump >= 3:
            commands[position] -= 1
        else:
            commands[position] += 1


        position += jump

        steps += 1

    return steps

SAMPLE_INP =\
"""0
3
0
1
-3
"""

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 5, 10)