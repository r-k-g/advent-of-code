import re

from lib import *
problem = aoc.Problem("2021/17: Trick Shot")
problem.preprocessor = ppr.I

class Probe:
    def __init__(self, x=0, y=0, xvel=0, yvel=0):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel

        self.max_h = self.y
    
    def do_step(self):
        self.x += self.xvel
        self.y += self.yvel

        self.yvel -= 1
        if self.xvel > 0:
            self.xvel -= 1
        elif self.xvel < 0:
            self.xvel += 1
        
        if self.y > self.max_h:
            self.max_h = self.y
    
    def in_area(self, x1, y1, x2, y2):
        # x1 and y1 are smallest values
        return x1 <= self.x <= x2 and y1 <= self.y <= y2

@problem.solver()
def solve(inp):
    m = re.match("target area: x=([-\d]+)..([-\d]+), y=([-\d]+)..([-\d]+)", inp)
    x1, x2, y1, y2 = [int(i) for i in m.groups()]
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])

    heights = set()
    successful = 0

    for xvel in range(0, x2 + 1):
        for yvel in range(-abs(y1) - 1, abs(y1) + 1):
            p = Probe(xvel=xvel, yvel=yvel)

            while p.x <= x2 and p.y >= y1:
                if p.in_area(x1, y1, x2, y2):
                    heights.add(p.max_h)
                    successful += 1
                    break
                p.do_step()

    return max(heights), successful

SAMPLE_INP = ("""target area: x=20..30, y=-10..-5""")

if __name__ == "__main__":
    problem.solve(SAMPLE_INP, 45, 112)