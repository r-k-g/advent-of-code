import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache, reduce
from copy import deepcopy

def constant_factory(value):
    return lambda: value

class Name:
    def __init__(self, ):
        pass
    
    def func(self):
        pass

with open('day_11_sa.txt', 'r') as inp:
    result = inp.read().strip().split('\n')

#result = [int(L) for L in result] # convert into ints

# result.split('\n\n') # split up by empty lines

# [g.split('\n') for g in result.split('\n\n')] # split up by empty lines, then by lines in sublists