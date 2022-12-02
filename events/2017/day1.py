from lib import *
helper = aoc.Helper("2017/01", "Inverse Captcha")

SAMPLE = """
123123
"""
helper.check_sample(SAMPLE, 0, 12)

inp = helper.get_input().strip()
inp = ppr.digits(inp)

def get_ahead(l, i, n):
    return l[(i+n) % len(l)]

total1 = 0
total2 = 0

for i in range(len(inp)):
    if inp[i] == get_ahead(inp, i, 1):
        total1 += inp[i]
    if inp[i] == get_ahead(inp, i, len(inp) // 2):
        total2 += inp[i]

print("Part 1:", total1)
print("Part 2:", total2)