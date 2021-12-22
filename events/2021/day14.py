from collections import Counter

from lib import *
problem = old_aoc.Problem("2021/14: Extended Polymerization")
problem.preprocessor = ppr.llsv

@problem.solver(part=1)
def part1(inp):
    template, rules = inp
    rules = {l.split(" -> ")[0]: l.split(" -> ")[1] for l in rules.split("\n")}

    for i in range(10):
        polymer = []
        for group in nwise(template, 2):
            if "".join(group) in rules:
                polymer.append(group[0] + rules["".join(group)] + group[1])
        template = "".join([i[:2] for i in polymer]) + polymer[-1][-1]

    c = Counter(template).most_common()
    p1 = c[0][1] - c[-1][1]

    return p1

@problem.solver(part=2)
def part2(inp):
    template, rules = inp
    debug = len(rules) == 127

    rules = {l.split(" -> ")[0]: l.split(" -> ")[1] for l in rules.split("\n")}

    pairs = Counter()
    for group in nwise(template, 2):
        pairs["".join(group)] += 1
    
    for i in range(40):
        new_pairs = Counter()
        for k in pairs:
            if k in rules:
                new_pairs[k[0] + rules[k]] += pairs[k]
                new_pairs[rules[k] + k[1]] += pairs[k]
        pairs = new_pairs
    
    characters = Counter()
    for k in pairs:
        characters[k[0]] += pairs[k]
    characters[template[-1]] += 1

    c = characters.most_common()
    p2 = c[0][1] - c[-1][1]

    return p2


SAMPLE_INP = ("""
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 1588, 2188189693529)