import aoc

helper = aoc.Helper("2021/01", "Sonar Sweep")

SAMPLE = """
199
200
208
210
200
207
240
269
260
263
"""
helper.check_sample(SAMPLE, 7, 5)


inp = [int(i) for i in helper.get_input().strip().split("\n")]

increased = 0
for i in range(1, len(inp)):
    if inp[i] > inp[i-1]:
        increased += 1
print("Part 1:", increased)

increased = 0
for i in range(3, len(inp)):
    if inp[i] > inp[i-3]:
        increased += 1
print("Part 2:", increased)