import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache, reduce
from copy import deepcopy

from lib import *
problem = aoc.Problem("2021/16: ???")
problem.preprocessor = ppr.I

HEX_TO_BIN = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

class Packet:
    def __init__(self, version, tid, literal, subpackets):
        self.version = version
        self.tid = tid
        self.literal = literal
        self.subpackets = subpackets
    
    def sum_versions(self):
        return self.version + sum(sp.sum_versions() for sp in self.subpackets)
    
    def __repr__(self):
        return f"Packet({self.version=} {self.tid=} {self.literal=} {self.subpackets=})"

@problem.solver()
def solve(inp):
    global data
    p1, p2 = 0, 0

    data = "".join(HEX_TO_BIN[i] for i in inp)

    print(parse())

    return (p1, p2)

def consume(n):
    global data

    val = ""

    if n > 1:
        val = data[:n]
        data = data[n:]
    else:
        while True:
            chunk = consume(5)
            val += chunk[1:]
            if chunk[0] == "0":
                break
    return val

def parse():
    version = int(consume(3), 2)
    tid = int(consume(3), 2)
    literal = None
    subpackets = []

    if tid == 4:
        literal = int(consume(-1), 2)
    else:
        ltid = int(consume(1), 2)
        if ltid == 0:
            length = int(consume(15), 2)
        elif ltid == 1:
            count = int(consume(11), 2)        

    return Packet(version, tid, literal, subpackets)

SAMPLE_INP = ("""
D2FE28
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 0, 0)