import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache, reduce
from copy import deepcopy

def constant_factory(value):
    return lambda: value

class Hexgame:

    dirmap = {
        'e': (2, 0),
        'w': (-2, 0),
        'ne': (1, -1), 
        'nw': (-1, -1), 
        'se': (1, 1), 
        'sw': (-1, 1)
        }

    def __init__(self, starting):
        self.tiles = starting

    def advance(self):
        self.expand()
        
        startstate = deepcopy(self.tiles)

        for t in startstate:
            b_around = 0
            for n in self.get_around(t):
                if n in startstate and not startstate[n]:
                    b_around += 1
    
            if startstate[t]:
                if b_around == 2:
                    self.tiles[t] = not self.tiles[t]
            else:
                if b_around == 0 or b_around > 2:
                    self.tiles[t] = not self.tiles[t]

    def expand(self):
        for t in deepcopy(self.tiles):
            for neighbour in self.get_around(t):
                self.tiles[neighbour] = self.tiles[neighbour] # let defaultdict do its thing
    
    def get_around(self, tile):
        x, y = tile
        around = list()
        for d in dirmap:
            around.append((x + dirmap[d][0], y + dirmap[d][1]))
        return around

    def count_black(self):
        black = 0
        for t in self.tiles:
            if not self.tiles[t]:
                black += 1
        return black

with open('day_24_inp.txt', 'r') as inp:
    result = inp.read().split('\n')

directions = list()

for l in result:
    stored, line = list(), list()
    for i in range(len(l)):
        stored.append(l[i])
        if l[i] in ('e', 'w'):
            line.append(''.join(stored))
            stored.clear()
    directions.append(line)

dirmap = {
    'e': (2, 0),
    'w': (-2, 0),
    'ne': (1, -1), 
    'nw': (-1, -1), 
    'se': (1, 1), 
    'sw': (-1, 1), 
}

tiles = defaultdict(constant_factory(True))

for dlist in directions:
    x, y = 0, 0
    for d in dlist:
        x += dirmap[d][0]
        y += dirmap[d][1]
    tiles[(x, y)] = not tiles[(x, y)]


g = Hexgame(tiles)
for i in range(100):
    g.advance()
    print(i)

print(g.count_black())