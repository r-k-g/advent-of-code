import re


def getsum1(group):
    setlist = [set(p) for p in group]
    setlist.remove(set())
    
    if len(setlist) > 1:
        return len(setlist[0].union(*setlist[1:]))
    else:
        return len(setlist[0])
    


def getsum2(group):
    setlist = [set(p) for p in group]
    setlist.remove(set())
    # print(setlist)
    
    if len(setlist) > 1:
        return len(setlist[0].intersection(*setlist[1:]))
    else:
        return len(setlist[0])
    


with open('day_6_inp.txt', 'r') as inp:
    lines = inp.readlines()

lines = ''.join(lines).split('\n')
newlines = list()
line = list()
for l in lines:
    line.append(l)
    if l == '':
        newlines.append(line.copy())
        line.clear()

lenl = list()

for l in newlines:
    lenl.append(getsum2(l))

print(sum(lenl) + getsum2(["wdfkpmalijbncuvr", "qhnmikpzaygxwsovej", ""]))
