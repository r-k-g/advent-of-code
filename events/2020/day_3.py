from day_3_inp import treemap

def travel(hor, ver):
    pos = 0
    treecount = 0
    m_len = len(treemap[0])

    for level in range(len(treemap))[::ver]:
        if treemap[level][pos % m_len] == '#':
            treecount += 1
        pos += hor
    
    return treecount

print(travel(3, 1))
print(travel(1,1)*travel(3,1)*travel(5,1)*travel(7,1)*travel(1,2))