from lib import *
problem = aoc.Problem("2021/07: The Treachery of Whales")
problem.preprocessor = ppr.csi

@problem.solver()
def solve(inp):
    positions = []

    for i in range(min(inp), max(inp) + 1):
        fuel1 = 0
        fuel2 = 0
        for x in inp:
            dist = abs(i-x)
            fuel1 += dist
            fuel2 += dist * (dist + 1) // 2
        positions.append(fuel1)
        positions.append(fuel2)
    
    return (min(positions[::2]), min(positions[1::2]))

SAMPLE_INP = ("""
16,1,2,0,4,2,7,1,2,14
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 37, 168)