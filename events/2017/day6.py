from lib import *
problem = aoc.Problem("2017/06: Memory Reallocation")
problem.preprocessor = lambda nums: [
    int(i) for i in nums.strip().split()
]

@problem.solver()
def solve(banks):
    seen = dict()

    cycles = 0

    while True:
        cycles += 1
        
        largest = max(banks)
        start = banks.index(largest)
        banks[start] = 0

        for i in range(1, largest + 1):
            ind = (start + i) % len(banks)
            banks[ind] += 1
        
        tuple_banks = tuple(banks)
        if tuple_banks in seen:
            break
        else:
            seen[tuple_banks] = cycles

    dist = cycles - seen[tuple_banks]

    return (cycles, dist)

if __name__ == "__main__":
    problem.solve("0 2 7 0", 5, 4)