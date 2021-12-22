from functools import reduce
import operator

from lib import *
problem = old_aoc.Problem("2021/16: Packet Decoder")
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

    def get_value(self):
        funcs = {
            0: lambda spv: sum(spv),
            1: lambda spv: reduce(operator.mul, spv),
            2: lambda spv: min(spv),
            3: lambda spv: max(spv),
            4: lambda _  : self.literal,
            5: lambda spv: int(spv[0] > spv[1]),
            6: lambda spv: int(spv[0] < spv[1]),
            7: lambda spv: int(spv[0] == spv[1])
        }
        return funcs[self.tid]([sp.get_value() for sp in self.subpackets])
    
    def __repr__(self):
        return f"Packet({self.version=} {self.tid=} {self.literal=} {self.subpackets=})"

@problem.solver()
def solve(inp):
    global data

    data = "".join(HEX_TO_BIN[i] for i in inp)
    outer = parse()
    return (outer.sum_versions(), outer.get_value())

def parse():
    version = int(consume(3), 2)
    tid = int(consume(3), 2)
    literal = None
    subpackets = []

    if tid == 4:
        literal = get_literal()
    else:
        ltid = int(consume(1), 2)
        if ltid == 0:
            length = int(consume(15), 2)
            start_size = len(data)
            while start_size - len(data) != length:
                subpackets.append(parse())
        elif ltid == 1:
            count = int(consume(11), 2)        
            for _ in range(count):
                subpackets.append(parse())

    return Packet(version, tid, literal, subpackets)

def consume(n):
    global data

    val = data[:n]
    data = data[n:]
    return val

def get_literal():
    chunks = []
    while True:
        chunk = consume(5)
        chunks.append(chunk[1:])
        if chunk[0] == "0":
            break
    return int("".join(chunks), 2)


if __name__ == "__main__":
    problem.solve()