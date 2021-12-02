import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter
from itertools import chain, combinations, permutations
from functools import lru_cache
from copy import deepcopy

class Ship:
    def __init__(self, heading):
        self.head_map = {
            'N': [1, 1],
            'S': [1, -1],
            'E': [0, 1],
            'W': [0, -1]
        }
        
        self.heading = heading
        
        self.headings = ['E', 'N', 'W', 'S']
        self.rot_pos = 0
        
        # east/west, north/south
        self.pos = [0, 0]
        self.moved = [0, 0]

        self.waypoint = [10, 1]
    
    def forw(self, amount, dire):
        for t in range(amount):
            self.moved[0] += self.waypoint[0]
            self.moved[1] += self.waypoint[1]

    def godire(self, amount, dire):
        self.waypoint[self.head_map[dire][0]] += amount * self.head_map[dire][1]
    
    def turn(self, amount, dire):
        
        if dire == 'R':
            for i in range(amount // 90):
                self.waypoint = [self.waypoint[1], -self.waypoint[0]]
        elif dire == 'L':
            for i in range(amount // 90):
                self.waypoint = [-self.waypoint[1], self.waypoint[0]]
    
    def get_manhattan(self):
        return sum([abs(i) for i in self.moved])



with open('day_12_inp.txt', 'r') as inp:
    result = inp.read().split('\n')

s = Ship('E')

for instr in result:
    if instr[:1] in ['E', 'N', 'W', 'S']:
        s.godire(int(instr[1:]), instr[:1])
    elif instr[:1] in ['R', 'L']:
        s.turn(int(instr[1:]), instr[:1])
    elif instr[:1] == 'F':
        s.forw(int(instr[1:]), instr[:1])

print(s.get_manhattan())