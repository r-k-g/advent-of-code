from lib import *
helper = aoc.Helper("2022/02", "Rock Paper Scissors")

SAMPLE = """
A Y
B X
C Z
"""
helper.check_sample(SAMPLE, 15, 12)

inp = helper.get_input().strip()
games = [game.split() for game in inp.split("\n")]

def score_game(enemy, you):
    s = 0
    if wins[enemy] == you:
        s += 6
    elif draws[enemy] == you:
        s += 3
    s += "XYZ".index(you) + 1
    return s

wins = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

draws = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

print("Part 1:", sum(score_game(*game) for game in games))

score = 0

for enemy, you in games:
    if you == "Z":
        play = wins[enemy]
    elif you == "Y":
        play = draws[enemy]
    else:
        play = (set("XYZ") - {wins[enemy], draws[enemy]}).pop()

    score += score_game(enemy, play)

print("Part 2:", score)