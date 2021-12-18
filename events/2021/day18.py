from itertools import permutations
import math

from lib import *
problem = aoc.Problem("2021/18: Snailfish")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(inp):
    big_l = snail_reduce(str_to_snailfish(inp[0]))
    for line in inp[1:]:
        new = snail_reduce(str_to_snailfish(line))
        big_l = snail_reduce(add_snailfish(big_l, new))
    
    final = get_magnitude(big_l)

    magnitudes = set()
    for num1, num2 in permutations(inp, r=2):
        num1 = snail_reduce(str_to_snailfish(num1))
        num2 = snail_reduce(str_to_snailfish(num2))
        snail_sum = snail_reduce(add_snailfish(num1, num2))
        magnitudes.add(get_magnitude(snail_sum))

    return (final, max(magnitudes))

def snail_reduce(l):
    while explodable(l) is not None or splittable(l) is not None:
        while (e := explodable(l)) is not None:
            l = explode(l, e)
        while (s := splittable(l)) is not None:
            l = split(l, s)
            if explodable(l) is not None:
                break
    return l

def explode(l, start):
    n1, n2 = l[start+1], l[start + 3]
    
    for i in range(start-1, -1, -1):
        if isinstance(l[i], int):
            l[i] += n1
            break
    for i in range(start+4, len(l)):
        if isinstance(l[i], int):
            l[i] += n2
            break
    l[start] = 0
    del l[start+1:start+5]
    return l

def explodable(l):
    depth = 0
    for i, item in enumerate(l):
        if item == "[":
            depth += 1
            if (depth == 5 
                and isinstance(l[i + 1], int)  
                and isinstance(l[i+3], int)):
                return i
        elif item == "]":
            depth -= 1
        
    return None

def split(l, start):
    n = l[start]
    n1, n2 = n//2, math.ceil(n/2)
    pair = ["[", n1, ",", n2, "]"]
    del l[start]
    for c in pair[::-1]:
        l.insert(start, c)
    return l

def splittable(l):
    for i, item in enumerate(l):
        if isinstance(item, int) and item >= 10:
            return i
    return None

def add_snailfish(l1, l2):
    return ["[", *l1, ",", *l2, "]"]

def str_to_snailfish(s):
    return [int(i) if i.isnumeric() else i for i in s]

def snail_to_str(l):
    return "".join([str(i) for i in l])

def get_magnitude(l):
    if isinstance(l, int):
        return l

    # convert into actual nested lists the first time
    if any([isinstance(i, str) for i in l]):
        l = eval(snail_to_str(l))

    if isinstance(l[0], int) and isinstance(l[1], int):
        return l[0]*3 + l[1] * 2
    else:
        return get_magnitude(l[0])*3 + get_magnitude(l[1])*2


SAMPLE_INP = ("""
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 4140, 3993)