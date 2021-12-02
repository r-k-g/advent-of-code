import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache, reduce
from copy import deepcopy


def combat(player1, player2):
    seen = set()

    while player1 and player2:
        c_round = (tuple(player1), tuple(player2))
        
        if c_round in seen:
            return 1, player1
        seen.add(c_round)

        c1, c2 = player1.popleft(), player2.popleft()

        if len(player1) >= c1 and len(player2) >= c2:
            winner = combat(deque(list(player1.copy())[:c1]), deque(list(player2.copy())[:c2]))[0]
        else:
            if c1 > c2:
                winner = 1
            elif c2 > c1:
                winner = 2
    
        if winner == 1:
            player1.extend([c1, c2])
        elif winner == 2:
            player2.extend([c2, c1])
    
    return winner, player1 if winner == 1 else player2
    

from day_22_inp import player1, player2


wincards = combat(player1, player2)[1]

wincards.reverse()
print(sum(x[0] * x[1] for x in list(enumerate(wincards, 1))))
