from lib import *
problem = old_aoc.Problem("2017/09: Stream Processing")
problem.preprocessor = ppr.I

@problem.solver()
def solve(inp):
    score, garbage = 0, 0

    level = 0
    ingarbage = False
    skip = False
    
    for i in inp:
        if skip:
            skip = False
        elif ingarbage:
            if i == ">":
                ingarbage = False
            elif i == "!":
                skip = True
            else:
                garbage += 1
        else:
            if i == "<":
                ingarbage = True
            if i == "{":
                level += 1
            if i == "}":
                score += level
                level -= 1

    return (score, garbage)

if __name__ == "__main__":
    problem.solve()