from day_2_inp import allpass

def part1():
    valid = 0

    for i in range(len(allpass))[::2]:
        lower, upper, c = allpass[i]
        passwd = allpass[i+1]

        if lower <= passwd.count(c) <= upper:
            valid += 1

    return valid

def part2():
    valid = 0

    for i in range(len(allpass))[::2]:
        passwd = allpass[i+1]
        ind_1, ind_2, l = allpass[i]

        if l in (passwd[ind_1-1], passwd[ind_2-1]):
            if passwd[ind_1-1] != passwd[ind_2-1]:
                valid += 1

    return valid

print(part1())
print(part2())