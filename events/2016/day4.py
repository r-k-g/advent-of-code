import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache, reduce
from copy import deepcopy

def constant_factory(value):
    return lambda: value

from lib import *
problem = aoc.Problem("2016/04: Security Through Obscurity")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(rooms):
    real_ids = []

    debug = len(rooms) < 10

    real_msgs = []

    for r in rooms:
        m = re.match("([a-z\-]+)-(\d+)\[(\w+)\]", r)
        encrypted, sector_id, checksum = m.groups()
        name = encrypted.replace("-", "")

        common = Counter(name).most_common()
        common.sort(key=lambda e: (-e[1], e))
        common = common[:5]


        if "".join(i[0] for i in common) == checksum:
            real_ids.append(int(sector_id))
            real_msgs.append(shift_words(encrypted, int(sector_id)))
        
        if debug:
            print(common, checksum)
        
    print(real_msgs)
    return sum(real_ids)

def shift_words(encrypted, shift):
    shift = shift % 25

    decrypted = []

    words = encrypted.split("-")
    for w in words:
        word = []
        for c in w:
            word.append(chr(97 + ((ord(c) - 97 + shift) % 26)))
        decrypted.append("".join(word))
    
    return " ".join(decrypted)

SAMPLE_INP =\
"""aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
"""

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 1514, 0)