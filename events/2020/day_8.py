import random, os, sys, re, statistics, copy
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain # flatten 1 deep nested list, have to *list of lists

class Gameboot:
    def __init__(self, instr):
        self.instr = instr
        self.instlen = len(self.instr)
        self.pos = 0
        
        self.accv = 0
        self.done = list()

        self.act_map = {
            'acc': self.acc,
            'jmp': self.jmp,
            'nop': self.nop
        }
    
    def acc(self):
        if self.pos + 1 in self.done:
            # print(self.accv)
            # exit()
            pass
        
        else:
            self.done.append(self.pos)
            self.accv += int(self.instr[self.pos][1])
            
            self.pos += 1
            if self.pos == self.instlen:
                print(self.accv)
            else:
                self.act_map[self.instr[self.pos][0]]()

    def jmp(self):
        if self.pos + int(self.instr[self.pos][1]) in self.done:
            # print(self.accv)
            # exit()
            pass
        
        else:
            self.done.append(self.pos)
            self.pos += int(self.instr[self.pos][1])
            
            if self.pos == self.instlen:
                print(self.accv)
            else:
                self.act_map[self.instr[self.pos][0]]()

    def nop(self):
        if self.pos + 1 in self.done:
            # print(self.accv)
            # exit()
            pass
        
        else:
            self.done.append(self.pos)
            self.pos += 1
            
            if self.pos == self.instlen:
                print(self.accv)
            else:
                self.act_map[self.instr[self.pos][0]]()

    def run(self):
        self.act_map[self.instr[0][0]]()


with open('day_8_inp.txt', 'r') as inp:
    result = [l.strip() for l in inp.readlines()]

instr = [l.split() for l in result]

# part 2
for i in range(len(instr)):
    if instr[i][0] in ('jmp', 'nop'):
        l = copy.deepcopy(instr)
        if instr[i][0] == 'jmp':
            l[i][0] = 'nop'
        else:
            l[i][0] = 'jmp'
        gb = Gameboot(l)
        gb.run()


gb = Gameboot(instr)
gb.run()