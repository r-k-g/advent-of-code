from collections import defaultdict

from lib import *
problem = old_aoc.Problem("2021/12: Passage Pathing")
problem.preprocessor = lambda inp: (
    line.split("-") for line in inp.strip().split("\n")
)

@problem.solver()
def solve(inp):
    all_paths1 = []
    all_paths2 = []

    graph = defaultdict(list)

    for c1, c2 in inp:
        graph[c1].append(c2)
        graph[c2].append(c1)
    
    allpaths1("start", graph, set(), [], all_paths1)
    allpaths2("start", graph, {"start"}, [], all_paths2, False)

    p1 = len(set([tuple(g) for g in all_paths1]))
    p2 = len(set([tuple(g) for g in all_paths2]))

    return (p1, p2)

def allpaths1(start, graph, visited, path, all):
    path.append(start)

    if start == "end":
        all.append(path.copy())

    if start.islower():
        visited.add(start)

    for adj in graph[start]:
        if adj not in visited:
            allpaths1(adj, graph, visited.copy(), path.copy(), all)

def allpaths2(start, graph, visited, path, all, doubled):
    path.append(start)

    if start == "end":
        visited.add(start)
        all.append(path.copy())

    elif start.islower() and doubled:
        visited.add(start)

    for adj in graph[start]:
        if adj not in visited:
            if not doubled and start.islower():
                allpaths2(adj, graph, visited.copy(), path.copy(), all, True)
                vis = visited.union({start})
                allpaths2(adj, graph, vis, path.copy(), all, False)
            
            else:
                allpaths2(adj, graph, visited.copy(), path.copy(), all, doubled)


SAMPLE_INP = ("""
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 10, 36)