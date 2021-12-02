import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter, defaultdict
from itertools import chain, combinations, permutations, product
from functools import lru_cache, reduce
from copy import deepcopy

def rotate(l):
    newl = list()
    for i in range(len(l[0])):
        newl.append(getcol(i, l)[::-1])
    
    return [''.join(sl) for sl in newl]
    
def flip(l):
    lcop = deepcopy(l)
    return [sl[::-1] for sl in l]

def getcol(col, l):
    return [sl[col] for sl in l]

def gettop(l):
    return l[0]

def getbot(l):
    return l[-1]

def getright(l):
    return getcol(len(l[0]) - 1, l)

def getleft(l):
    return getcol(0, l)

def stripouter(t):
    newl = deepcopy(t)
    newl = [l[1:-1] for l in newl[1:-1]]
    return newl

def joinimg(imgs):

    #l = [[['abc', '123'], ['def', '456'], ['ghi', '789']], [['jkl', '012'], ['mno', '345'], ['pqr', '678']]]
    #
    #result = '''
    #abcdefghi
    #123456789
    #jklmnopqr
    #012345678
    #'''

    bigimg = list()
    for tl in imgs:
        linegroup = [str() for i in range(len(tl[0]))]
        for tile in tl:
            for line in range(len(tile)):
                linegroup[line] += tile[line]
        bigimg.extend(linegroup)
    return bigimg
            
def findmatch(tileid, ar, side):
    """Find a match for a given tile arrangments given side.
    
    Return the id of the match if it exists, None otherwise.
    """
    
    if side == 'top':
        for tid in d:
            if tid == tileid:
                continue
            for a in d[tid]:
                pass
                

    elif side == 'left':
        pass

    elif side == 'right':
        pass

    elif side == 'bottom':
        pass
    

with open('day_20_inp.txt', 'r') as inp:
    result = inp.read()

result = [g.split('\n') for g in result.split('\n\n')]

tiles = {k[5:-1]:[[s for s in  v]] for k, *v in result}

for k in tiles: # add all variations
    og = tiles[k][0]
    l = deepcopy(og)
    tiles[k].append(flip(l))
    for i in range(3):
        l = rotate(l)
        tiles[k].append(l)
        tiles[k].append(flip(l))

ides = list()

bigimg = [[None for i in range(12)] for x in range(12)]
bigimg[0][0] = ['.#.#.#..#.',
                '...#..#.##',
                '.##.##...#',
                '#.........',
                '...#.....#',
                '#.#.#.....',
                '#.##.....#',
                '..#.....##',
                '#.#....##.',
                '....##..##',]

d = deepcopy(tiles)
del d['3221']

counter = 0
for y in range(12):
    for x in range(12):
        if bigimg[y][x] is not None:
            continue
        
        else:
            last = bigimg[y][x-1] if x != 0 else bigimg[y-1][-1]
            if last is None:
                continue
            if y == 0: # check left
                for tileid in d:
                    for ar in d[tileid]:
                        if getleft(ar) == getright(last):
                            bigimg[y][x] = ar
                            del d[tileid]
                            break
                    else:
                        continue
                    break
            
            elif x == 0: # leftmost column, check above
                for tileid in d:
                    for ar in d[tileid]:
                        if gettop(ar) == getbot(bigimg[y-1][0]):
                            bigimg[y][x] = ar
                            del d[tileid]
                            break
                    else:
                        continue
                    break

            else: # check left
                for tileid in d:
                    for ar in d[tileid]:
                        if getleft(ar) == getright(last):
                            bigimg[y][x] = ar
                            del d[tileid]
                            break
                    else:
                        continue
                    break


bigimg = [[stripouter(t) for t in r] for r in bigimg]
img = joinimg(bigimg)
variations = [img, flip(img)]

for i in range(3):
    img = rotate(img)
    variations.append(img)
    variations.append(flip(img))

                  # 
#    ##    ##    ###
 #  #  #  #  #  #   

inds = [(18, 0), 
(0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1), 
(1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2)]

mon_count = list()

for v in variations:
    m = 0
    for y in range(len(v) - 2):
        for x in range(len(v[0]) - 19):
            chunk = [v[y][x:x+20] for y in range(y, y+3)]

            for xin, yin in inds:
                if chunk[yin][xin] == '#':
                    continue
                else:
                    break
                
            else: # monster found
                for xin, yin in inds:
                    v[y + yin] = list(v[y + yin])
                    v[y + yin][x + xin] = 'O'
                    v[y + yin] = ''.join(v[y + yin])
                m += 1
    mon_count.append(m)

print(mon_count)
for line in variations[2]:
    print(line)