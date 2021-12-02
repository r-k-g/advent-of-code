import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache, reduce
from copy import deepcopy

class Node:
    def __init__(self, data):
        self.val = data
        self.right = None
        self.left = None
    
    def __repr__(self):
        return self.val
    
    def __str__(self):
        return str(self.val)




with open('day_23_inp.txt') as f:
    inp = [int(i) for i in f.read().strip().split(',')]

nodes = dict()

# create nodes for starting input
last = None
for i in inp:
    node = Node(i)
    nodes[i] = node
    
    if last is not None:
        node.left = last
        nodes[last.val].right = node
    
    last = node

# fill in to 1 mil
for i in range(10, 1_000_001):
    node = Node(i)
    nodes[i] = node
    
    if last is not None:
        node.left = last
        nodes[last.val].right = node
    
    last = node

# attach ends
first = nodes[inp[0]]
last.right = first
first.left = last

cur = first
for i in range(10_000_000):
    
    if i % 500_000 == 0_0:
        print(i)
    
    cur_val = cur.val

    p1 = cur.right
    p2 = p1.right
    p3 = p2.right

    cur.right = p3.right
    cur.right.left = cur

    dest_val = cur_val - 1 or 1_000_000
    while dest_val in (p1.val, p2.val, p3.val):
        dest_val = dest_val - 1 or 1_000_000

    dest = nodes[dest_val]

    p3.right = dest.right
    p3.right.left = p3
    dest.right = p1
    p1.left = dest

    cur = cur.right

while cur.val != 1:
    cur = cur.right

print(cur.right.val, cur.right.right.val, cur.right.val * cur.right.right.val)