from math import ceil
with open('day_5_inp.txt', 'r') as inp:
    lines = inp.readlines()
lines = [l.strip() for l in lines]

row = 0
column = 0

def getrow(bpass, srange):
    global row
    if bpass[0] == 'F': # lower half
        srange[1] -= (srange[1]-srange[0])//2 + 1
    
    elif bpass[0] == 'B':
        srange[0] += (srange[1]-srange[0])//2 + 1
    
    if len(bpass) == 1:
        row = ''.join([str(s) for s in set(srange)])
        return

    getrow(bpass[1:], srange)

def getcol(bpass, srange):
    global column
    if bpass[0] == 'L': # lower half
        srange[1] -= (srange[1]-srange[0])//2 + 1
    
    elif bpass[0] == 'R':
        srange[0] += (srange[1]-srange[0])//2 + 1
    
    if len(bpass) == 1:
        column = ''.join([str(s) for s in set(srange)])
        return

    getcol(bpass[1:], srange)

ids = list()
seats = list()
allseats = [(r, c) for r in range(1, 127) for c in range(0, 8)]

for bpass in lines:
    getrow(bpass, [0, 127])
    getcol(bpass, [0, 7])
    ids.append(int(row)*8 + int(column))
    seats.append((int(row), int(column)))

print(max(ids))

ids.sort()

for i in range(len(ids)-1):
    if ids[i + 1]  != ids[i] + 1:
        print(ids[i]+1)