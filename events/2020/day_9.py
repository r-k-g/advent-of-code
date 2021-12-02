import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter
from itertools import chain, combinations

class XCipher:
    def __init__(self, prelen):
        self.prelen = prelen
        self.failn = None
    
    def find_invalid(self, data):
        for i in range(len(data)):
            if i < self.prelen:
                continue

            for n1, n2 in list(combinations(data[i-self.prelen: i], 2)):
                if n1 + n2 == data[i]:
                    break 
                else:
                    continue
            else:
                print(data[i])
                self.failn = data[i]

    def find_cont(self, data):
        allcont = deque()
        for i in range(2, len(data)):
            allcont.extend([data[p:p+i] for p in range(0, len(data) - (i-1))])
        
        for g in allcont:
            if sum(g) == self.failn:
                print(sum([min(g), max(g)]))
                break


with open('day_9_inp.txt', 'r') as inp:
    result = [int(l.strip()) for l in inp.readlines()]

xc = XCipher(25)
xc.find_invalid(result)
xc.find_cont(result)