from collections import deque
import re

with open('day_4_inp.txt', 'r') as inp:
    lines = inp.readlines()

passports = re.split('\n\n', ''.join(lines))
for i in range(len(passports)):
    passports[i] = passports[i].split()
    for ele in range(len(passports[i])):
        passports[i][ele] = passports[i][ele].split(':')
    
    passports[i] = dict(passports[i])

def part1(passports):
    valid = 0
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for p in passports:
        if all(field in p for field in required):
            valid += 1
    return valid


def part2(passports):
    valid = 0
    for i in passports:
        try:
            if len(i['byr']) == 4 and int(i['byr']) >= 1920 and int(i['byr']) <= 2002:
                if len(i['iyr']) == 4 and int(i['iyr']) >= 2010 and int(i['iyr']) <= 2020:
                    if len(i['eyr']) == 4 and int(i['eyr']) >= 2020 and int(i['eyr']) <= 2030:
                        if (i['hgt'][-2:]=='in' and int(i['hgt'][:-2]) >= 59 and int(i['hgt'][:-2]) <= 76) or (i['hgt'][-2:]=='cm' and int(i['hgt'][:-2]) >= 150 and int(i['hgt'][:-2]) <= 193):
                            if i['hcl'][0]=='#' and len(i['hcl']) == 7 and i['hcl'][1:].isalnum():
                                if i['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                    if len(i['pid']) == 9 and i['pid'].isnumeric():
                                        valid += 1
        except KeyError:
            continue
    return valid

print(part1(passports))
print(part2(passports))