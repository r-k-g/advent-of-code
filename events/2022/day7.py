from lib import *
helper = aoc.Helper("2022/07", "No Space Left On Device")

SAMPLE = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
helper.check_sample(SAMPLE, 95437, 24933642)

inp = helper.get_input().strip().split("\n")

class Computer:
    def __init__(self):
        self.contents = {"/": {"SIZE": 0}}
    
    def get_current(self, path):
        pwd = self.contents
        for folder in path:
            pwd = pwd[folder]
        return pwd

    def add_folder(self, path, name, contents):
        self.get_current(path)[name] = contents

    def add_size(self, path, size):
        for i in range(1, len(path) + 1):
            self.get_current(path[:i])["SIZE"] += size

computer = Computer()

path = []
for line in inp:
    line = line.split()
    if line[1] == "cd":
        if line[2] == "..":
            path.pop()
        else:
            path.append(line[2])
    elif line[1] != "ls":
        if line[0]  == "dir":
            computer.add_folder(path, line[1], {"SIZE": 0})
        else:
            # computer.add_folder(path, line[1], int(line[0]))
            computer.add_size(path, int(line[0]))

total = 0
valid = []

queue = [["/"]]
full = computer.contents["/"]["SIZE"]
minsize = full - 40000000

while queue:
    path = queue.pop(0)
    contents = computer.get_current(path)

    if contents["SIZE"] <= 100000:
        total += contents["SIZE"]
    
    if contents["SIZE"] >= minsize:
        valid.append(contents["SIZE"])

    for name in contents:
        if isinstance(contents[name], dict):
            newpath = path.copy()
            newpath.append(name)
            queue.append(newpath)

print("Part 1:", total)
print("Part 2:", min(valid))