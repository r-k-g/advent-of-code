import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache
from copy import deepcopy

def constant_factory(value):
    return lambda: value

with open('day_14_inp.txt', 'r') as inp:
    result = inp.read().split('\n')

mem = defaultdict(constant_factory('0'*36))

for line in result:
    if line.startswith('mask = '):
        mask = line.split(' = ')[1]
    else:
        mem_in, num = line.split(' = ')
        mem_in = mem_in[4:-1]
        num = f'{int(num):036b}'

        masked = list(f'{int(mem_in):036b}')
        
        for i in range(36):
            if mask[i] == 'X':
                masked[i] = 'X'
            elif mask[i] == '1':
                #print('true')
                masked[i] = '1'
            else:
                pass
        mem_indices = list()

        x_indices = [i for i in range(len(masked)) if masked[i] == 'X']

        for combo in list(product(['0', '1'], repeat=len(x_indices))):
            mem_ver = masked.copy()
            for i in range(len(combo)):
                mem_ver[x_indices[i]] = combo[i]
            mem_indices.append(''.join(mem_ver))

        for i in mem_indices:
            mem[int(i, 2)] = num

print(sum([int(x, 2) for x in mem.values()]))