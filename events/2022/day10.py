from lib import *
helper = aoc.Helper("2022/10", "Cathode-Ray Tube")

inp = helper.get_input().strip()
inp = [line.split() for line in inp.split("\n")]

crt = [[" " for w in range(40)] for h in range(6)]
signal_sum = 0
def out_signal(x, cycle):
    global signal_sum, crt # I'm sorry

    if cycle in (20, 60, 100, 140, 180, 220):
        signal_sum += x * cycle

    adj = cycle - 1
    if abs(x - (adj % 40)) <= 1:
        crt[(adj) // 40][adj % 40] = "#"


x = 1
cycle = 0
for cmd in inp:
    if len(cmd) == 2:
        _, n = cmd
        n = int(n)
        for _ in range(2):
            cycle += 1
            out_signal(x, cycle)
        x += n
    else:
        cycle += 1
        out_signal(x, cycle)


print("Part 1:", signal_sum)
print("Part 2:\n",
    "\n".join("".join(c for c in l) for l in crt)
)