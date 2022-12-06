from lib import *
helper = aoc.Helper("2022/06", "Tuning Trouble")

SAMPLE = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""
helper.check_sample(SAMPLE, 7, 19)

def find_marker(data, unique):
    for c, group in enumerate(nwise(data, unique), start=unique):
        if len(set(group)) == unique:
            break
    return c

inp = helper.get_input().strip()

print("Part 1:", find_marker(inp, 4))
print("Part 2:", find_marker(inp, 14))