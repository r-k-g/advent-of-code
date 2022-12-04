from lib import *
helper = aoc.Helper("2022/04", "Camp Cleanup")

SAMPLE = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
helper.check_sample(SAMPLE, 2, 4)

assignments = helper.get_input().strip().split("\n")

overlap = 0
full_overlap = 0

for assignment in assignments:
    l, r = assignment.split(",")
    l = [*map(int, l.split("-"))]
    r = [*map(int, r.split("-"))]
    
    setl = set(range(l[0], l[1] + 1))
    setr = set(range(r[0], r[1] + 1))

    if setl & setr in (setl, setr):
        full_overlap += 1

    if len(setl & setr):
        overlap += 1

print("Part 1:", full_overlap)
print("Part 2:", overlap)