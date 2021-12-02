import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache, reduce
from copy import deepcopy

def constant_factory(value):
    return lambda: value


with open('day_25_inp.txt', 'r') as inp:
    result = inp.read().strip().split('\n')

result = [int(L) for L in result] # convert into ints

pub_card = result[0]
pub_door = result[1]

found = None

ans_card = 1
ans_door = 1

subj = 7
transf = 1
while True:
    if transf == pub_card:
        print(ans_card)
        break
    elif transf == pub_door:
        print(ans_door)
        break

    transf = (transf * subj) % 20201227
    ans_card = (ans_card * pub_door) % 20201227
    ans_door = (ans_door * pub_card) % 20201227