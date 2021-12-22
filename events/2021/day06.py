from collections import Counter

from lib import *
problem = old_aoc.Problem("2021/06: Lanternfish")
problem.preprocessor = ppr.csi

@problem.solver()
def solve(fishes):
    days = 256

    fishes = Counter(fishes)

    for d in range(days):
        school = fishes.copy()

        for time in school:
            if time == 0:
                fishes[8] += school[time]
                fishes[0] -= school[time]
                fishes[6] += school[time]
            else:
                fishes[time] -= school[time]
                fishes[time-1] += school[time]

        if d == 79:
            count1 = sum(fishes.values())

    count2 = sum(fishes.values())

    return (count1, count2)

SAMPLE_INP = ("""
3,4,3,1,2
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 5934, 26984457539)