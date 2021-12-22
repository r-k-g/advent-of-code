from lib import *
problem = old_aoc.Problem("2021/10: Syntax Scoring")
problem.preprocessor = ppr.lsv

CLOSINGS = {"(": ")", "[": "]", "{": "}", "<": ">"}
ERROR_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}

@problem.solver()
def solve(inp):
    error_score, completion_scores = 0, []

    for line in inp:
        invalid, result = process_line(line)
        if invalid:
            error_score += ERROR_POINTS.get(result, 0)
        else:
            score = 0
            for i in result:
                score = (score * 5) + " )]}>".index(i)
            completion_scores.append(score)
    
    completion_scores.sort()
    middle = completion_scores[len(completion_scores)//2]

    return (error_score, middle)

def process_line(line):
    """Return a tuple of form (bool invalid, invalid char|closing sequence)."""
    opened = []
    for i in line:
        if i in CLOSINGS.keys():
            opened.append(i)
        if i in CLOSINGS.values():
            if i == CLOSINGS[opened[-1]]:
                opened.pop()
            else:
                return True, i
    return False, "".join([CLOSINGS[i] for i in opened[::-1]])


SAMPLE_INP = ("""
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 26397, 288957)