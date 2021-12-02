import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache
from copy import deepcopy

def evaluate(line):
    line = list(line)

    brackets = findbrackets(line)
    if brackets:
        for i in range(len(brackets)):
            pair = findbrackets(line)[0]
            line = l_replace(line, [pair[0], pair[1]], evaluate(line.copy()[pair[0] + 1: pair[1]]))
    
    if len(line) > 1:
        if '+' in line and ('-' in line or '*' in line):
            line = brackitify(line)
            while '(' in line or ')' in line:
                pair = findbrackets(line)[0]
                line = l_replace(line, [pair[0], pair[1]], [str(eval(''.join(line[pair[0] + 1: pair[1]])))])
        
        else:
            for i in range(((len(line) + 1) // 2) - 1):
                line = l_replace(line, [0, 2], [str(eval(''.join(line[:3])))])
        
        return [str(eval(''.join(line)))]


def findbrackets(line: str) -> list:
    """Find outermost pairs of matching brackets in a string or list.
    
    Returns list of tuples with indeces inclusive.
    """

    opened = False
    startstop = list()
    level = 0
    pair = list()
    for i in range(len(line)):
        if line[i] == '(':
            if not opened:
                opened=True
                pair.append(i)
            level += 1

        elif line[i] == ')':
            level -= 1

        if level == 0 and opened:
            pair.append(i)
            startstop.append(tuple(pair))
            pair.clear()
            opened = False

    return startstop

def l_replace(l: list, inds: list, r:list) -> list:
    """Replace part of a list l from inds[0] to inds[1] inclusive with r"""

    before, after = l[:inds[0]], l[inds[1] + 1:]
    return before + r + after

def brackitify(line: list) -> list:
    """Add brackets around addition."""

    line = line.copy()
    indeces = list()
    started = False

    for i in range(len(line)):
        if line[i] == '+' and not started:
            started = True
            indeces.append(i - 1)
        
        elif line[i] in ['*', '-'] and started:
            started = False
            indeces.append(i)

    for i in range(len(indeces)):
        line.insert(indeces[i] + i, ')' if i%2 else '(')
    
    if started:
        line.append(')')
    
    return line


with open('day_18_inp.txt', 'r') as inp:
    result = inp.read().split('\n')

values = list()
for l in result:
    values.append(int(''.join(evaluate(l))))

print(sum(values))