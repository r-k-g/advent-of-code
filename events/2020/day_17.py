import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache
from copy import deepcopy

def constant_factory(value):
    return lambda: value

class Pocket:
    def __init__(self, starting):
        self.cubemap = defaultdict(constant_factory('.'))
        for y in range(len(starting)):
            for x in range(len(starting[0])):
                self.cubemap[x, y, 0, 0] = starting[y][x]
        
        self.x_range, self.y_range, self.z_range, self.w_range = [0, len(starting[0])], [0, len(starting)], [0, 1], [0, 1]

    def widen(self):
        self.x_range[0] -= 1
        self.x_range[1] += 1
        self.y_range[0] -= 1
        self.y_range[1] += 1
        self.z_range[0] -= 1
        self.z_range[1] += 1
        self.w_range[0] -= 1
        self.w_range[1] += 1
        
        for y in range(self.y_range[0], self.y_range[1] + 1):
            for x in range(self.x_range[0], self.x_range[1] + 1):
                for z in range(self.z_range[0], self.z_range[1] + 1):
                    for w in range(self.w_range[0], self.w_range[1] + 1):
                        if not (x, y, z, w) in self.cubemap:
                            self.cubemap[(x, y, z, w)] = self.cubemap[(x, y, z, w)]

    def cycle(self):
        self.widen()
        self.startstate = dict(deepcopy(self.cubemap))

        for c in self.startstate:
            if self.startstate[c] == '#':
                if self.get_around(c) in (2, 3):
                    self.cubemap[c] = '#'
                else:
                    self.cubemap[c] = '.'
            
            else: # inactive
                if self.get_around(c) == 3:
                    self.cubemap[c] = '#'
                else:
                    self.cubemap[c] = '.'
        
        self.x_range[0] -= 1
        self.x_range[1] += 1
        self.y_range[0] -= 1
        self.y_range[1] += 1
        self.z_range[0] -= 1
        self.z_range[1] += 1
        self.w_range[0] -= 1
        self.w_range[1] += 1

    def get_around(self, c):
        active = 0
        for x in range(c[0] - 1, c[0] + 2):
            for y in range(c[1] - 1, c[1] + 2):
                for z in range(c[2]-1, c[2] + 2):
                    for w in range(c[3]-1, c[3] + 2):  
                        try:
                            if (x, y, z, w) != c and self.startstate[(x,y,z, w)] == '#':
                                active += 1
                        except KeyError:
                            self.cubemap[(x, y, z, w)] = self.cubemap[(x, y, z, w)]
        return active
    
    def get_active(self):
        total = 0
        for c in self.cubemap:
            if self.cubemap[c] == '#': 
                total += 1
        return total


with open('day_17_inp.txt', 'r') as inp:
    result = inp.read().split('\n')

p = Pocket(result)
for i in range(6):
    p.cycle()

print(p.get_active())