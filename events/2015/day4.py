import hashlib

from lib import *
problem = old_aoc.Problem("2015/04: The Ideal Stocking Stuffer")
problem.preprocessor = ppr.I

@problem.solver()
def solve(inp):

    return get_hashnum(inp, 5), get_hashnum(inp, 6)

def get_hashnum(key, zeros):
    n = 0
    while True:
        full = key + str(n)
        if hashlib.md5(full.encode()).hexdigest().startswith("0" * zeros):
            return n
        n += 1

if __name__ == "__main__":
    problem.solve()