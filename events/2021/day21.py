from itertools import count, cycle, islice, product
from functools import lru_cache

from lib import *
problem = aoc.Problem("2021/21: Dirac Dice")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(inp):
    part1 = 0
    die = cycle(range(1, 101))

    # 0 index position and just add one for scoring
    p1pos = p1start = int(inp[0].split()[-1]) - 1
    p2pos = p2start = int(inp[1].split()[-1]) - 1

    p1turn = True

    p1_score = 0
    p2_score = 0
    for rolls in count(3, step=3):
        if p1turn:
            p1pos = (p1pos + sum(islice(die, 3))) % 10
            p1_score += p1pos + 1
        else:
            p2pos = (p2pos + sum(islice(die, 3))) % 10
            p2_score += p2pos + 1

        if p1_score >= 1000:
            part1 =  p2_score * rolls
            break
        elif p2_score >= 1000:
            part1 =  p1_score * rolls
            break
        
        p1turn = not p1turn
    
    return part1, max(game(p1start, p2start, 0, 0, True))


ALL_ROLLS = [sum(rolls) for rolls in product([1,2,3], repeat=3)]

@lru_cache(maxsize=None)
def game(p1pos, p2pos, p1score, p2score, p1turn):
    p1won, p2won = 0, 0
    for rolls in ALL_ROLLS:
        if p1turn:
            new_p1pos = (p1pos + rolls) % 10
            new_p1score = p1score + new_p1pos + 1
            if new_p1score >= 21:
                p1won += 1
            else:
                wins1, wins2 = game(new_p1pos, p2pos, new_p1score, p2score, False)
                p1won += wins1
                p2won += wins2
        else:
            new_p2pos = (p2pos + rolls) % 10
            new_p2score = p2score + new_p2pos + 1
            if new_p2score >= 21:
                p2won += 1
            else:
                wins1, wins2 = game(p1pos, new_p2pos, p1score, new_p2score, True)
                p1won += wins1
                p2won += wins2
    return p1won, p2won

SAMPLE_INP = ("""
Player 1 starting position: 4
Player 2 starting position: 8
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 739785, 444356092776315)