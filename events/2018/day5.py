from lib import *
problem = aoc.Problem("2018/05: Alchemical Reduction")
problem.preprocessor = lambda e: e.strip()

@problem.solver()
def solve(polymer):
    lengths = []
    for i in range(65, 91):
        p = polymer.replace(chr(i), "")
        p = p.replace(chr(i).lower(), "")
        lengths.append(final_length(p))

    return (final_length(polymer), min(lengths))

def final_length(polymer):
    reactors = []
    for i in range(65, 91):
        reactors.append(chr(i) + chr(i).lower())
        reactors.append(chr(i).lower() + chr(i))
    while any([r in polymer for r in reactors]):
        for r in reactors:
            if r in polymer:
                polymer = polymer.replace(r, "")
    return len(polymer)

SAMPLE_INP =\
"""dabAcCaCBAcCcaDA
"""

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 10, 4)