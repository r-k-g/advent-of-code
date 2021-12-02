import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product, cycle
from functools import lru_cache
from copy import deepcopy
from prog_indicators import Bar

class Name:
    def __init__(self, ):
        pass
    
    def func(self):
        pass



def allindices(li, val):
    return [i for i, x in enumerate(li) if x == val]


def game(starting):
    turns = 0
    positions = defaultdict(list)
    last = None

    while True:
        n = starting[turns % len(starting)]
        turns += 1
        
        if turns <= len(starting):
            val = n
        else:
            if len(positions[last]) == 1:
                val = 0
            else:
                indc = positions[last]
                val = indc[-1] - indc[-2]
        positions[val].append(turns - 1)
        last = val

        if turns == 30000000:
            print(val)
            break

inp = [11,0,1,10,5,19]
game(inp)