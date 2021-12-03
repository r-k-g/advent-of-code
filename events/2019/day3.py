from lib import *
problem = aoc.Problem("2019/03: Crossed Wires")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(inp):
    p1, p2 = 0, 0

    wires = []
    list_wires = []

    d = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

    for wire in inp:
        x, y = 0, 0
        w = set()
        list_w = [(0, 0)] + list()

        for move in wire.split(","):
            direction = move[:1]
            amount = int(move[1:])
            
            for i in range(amount):
                x += d[direction][0]
                y += d[direction][1]

                w.add((x, y))
                list_w.append((x, y))
        
        wires.append(w)
        list_wires.append(list_w)

    w1, w2 = wires
    overlap = wires[0].intersection(wires[1])
    closest = min(overlap, key=lambda e: abs(e[0]) + abs(e[1]))
    p1 = abs(closest[0]) + abs(closest[1])
    
    def get_steps(e):
        return list_wires[0].index(e) + list_wires[1].index(e)

    steps_closest = min(overlap, key=get_steps)
    
    p2 = get_steps(steps_closest)

    return (p1, p2)


if __name__ == "__main__":
    problem.solve()