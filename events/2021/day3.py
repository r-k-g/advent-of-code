from collections import Counter, defaultdict

from lib import *
problem = aoc.Problem("2021/03: Binary Diagnostic")
problem.preprocessor = ppr.lsv

def most_common_col(l, col):
    column = [i[col] for i in l]
    common = Counter(column).most_common()
    if common[0][1] == common [1][1]:
        return "TIE"
    else:
        return common[0][0]

@problem.solver(part=1)
def part1(inp):
    gamma = ["0"] * len(inp[0])
    ones = defaultdict(int)
    for v in inp:
        for i in range(len(v)):
            if v[i] == "1":
                ones[i] += 1
    
    for i in ones:
        if ones[i] > (len(inp) - ones[i]):
            gamma[i] = "1"

    gamma = "".join(gamma)
    ep = ""
    for i in gamma:
        ep += "0" if i == "1" else "1"
    
    return int(gamma, 2) * int(ep, 2)

@problem.solver(part=2)
def part2(inp):
    co2 = inp.copy()
    oxy = inp.copy()

    for x in range(len(inp[0])):
        common = most_common_col(oxy, x)

        if common == "TIE":
            oxy = [i for i in oxy if i[x] == "1"]
        else:
            oxy = [i for i in oxy if i[x] == common]

        if len(oxy) == 1:
            break
    
    for x in range(len(inp[0])):
        common = most_common_col(co2, x)

        if common == "TIE":
            co2 = [i for i in co2 if i[x] == "0"]
        else:
            co2 = [i for i in co2 if i[x] != common]

        if len(co2) == 1:
            break
    

    return int(oxy[0], 2) * int(co2[0], 2)

SAMPLE_INP =\
"""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 198, 230)