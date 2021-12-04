from lib import *
problem = aoc.Problem("2021/04: Giant Squid")
problem.preprocessor = ppr.llsv


@problem.solver()
def solve(inp):
    p1, p2 = 0, 0

    # process input further
    nums, *_boards = inp
    nums = [int(i) for i in nums.split(",")]

    boards = []
    for b in _boards:
        board = b.split("\n")
        board = [[int(i) for i in row.split()] for row in board]
        boards.append(board)
    
    # blank copy of boards, 0 = empty, 1=hit
    scores = [
        [[0] * len(r) for r in board]
        for board in boards
    ]

    winboard = -1
    have_won = set()

    for draw in nums:
        for b in range(len(boards)):
            for row in range(len(boards[b])):
                for i in range(len(boards[b][row])):
                    if boards[b][row][i] == draw:
                        scores[b][row][i] = 1

        for b in range(len(scores)):
            for row in range(len(scores[b])):
                if checkrow(scores[b], row):
                    winboard = b
                    have_won.add(b)

                    if len(have_won) == len(boards):
                        p2 = sum_unmarked(boards[winboard], scores[winboard]) * draw
                        return (p1, p2)

            for col in range(len(scores[b][0])):
                if checkcol(scores[b], col):
                    winboard = b
                    have_won.add(b)

                    if len(have_won) == len(boards):
                        p2 = sum_unmarked(boards[winboard], scores[winboard]) * draw
                        return (p1, p2)

        if p1 == 0 and winboard >= 0:
            p1 = sum_unmarked(boards[winboard], scores[winboard]) * draw

def sum_unmarked(board, marks):
    to_sum = []

    for row in range(len(marks)):
        for i in range(len(marks[row])):
            if marks[row][i] == 0:
                to_sum.append(board[row][i])
    
    return sum(to_sum)

def checkrow(board, row):
    return all([i for i in board[row]])

def checkcol(board, col):
    return all([i[col] for i in board])

SAMPLE_INP =\
"""7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 4512, 1924)