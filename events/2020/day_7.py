import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter

with open('day_7_inp.txt', 'r') as inp:
    result = inp.readlines() # split up into lines

bagrules = dict()

for l in result:
    line = l.split(' contain ')
    bagrules[line[0].strip().replace('bags', 'bag')] = [(i[2:].strip().replace('bags', 'bag'), i[:1]) for i in line[1].split(', ')]

# print(bagrules)

inv_bagrules = [(v, k) for k, v in bagrules.items()]
# [([('dull lavender bag', '1')], 'clear maroon bag')]

def cancontain1(b):
    if bagrules[b][0][0] == 'other bag':
        return False
    elif "shiny gold bag" in [i[0] for i in bagrules[b]]:
        return True
    else:
        return any(cancontain1(i[0]) for i in bagrules[b])


def part1():
    total = 0
    for b in bagrules:
        if cancontain1(b):
            total += 1
    return total


bags = 1
def cancontain2(bag):
    global bags

    if bagrules[bag][0][0] != 'other bag':
        for i in bagrules[bag]:
            bags += int(i[1])
            for x in range(int(i[1])):
                cancontain2(i[0])

    else:
        return 1


print(part1())
cancontain2('shiny gold bag')
print(bags - 1)