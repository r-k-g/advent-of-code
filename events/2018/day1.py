import time

def part1(inp):
    return(eval(inp))

def part2(inp): # slow
    seen = set()
    val = 0
    seen.add(val)

    while True:
        for op in inp:
            val = eval(f"{val}{op}")
            if val in seen:
                print("HERE")
                return val
            seen.add(val)

def main():
    with open("day1_inp.txt") as f:
        contents = f.read()
    inp1 = contents.replace("\n", "")
    inp2 = contents.split("\n")
    
    print(f"Part 1: {part1(inp1)}")
    print(f"Part 2: {part2(inp2)}")

if __name__ == "__main__":
    main()