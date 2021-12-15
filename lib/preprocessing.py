def I(s):
    return s.strip()
def identity(s):
    return s

#
# Space/comma/line separated values/integers
#

def ssv(s):
    return [v.strip() for v in s.strip().split(" ")]
def ssi(s):
    return [int(v.strip()) for v in s.strip().split(" ")]
def csv(s):
    return [v.strip() for v in s.strip().split(",")]
def csi(s):
    return [int(v.strip()) for v in s.strip().split(",")]
def lsv(s):
    return [l.strip() for l in s.strip().split("\n")]
def lsi(s):
    return [int(l.strip()) for l in s.strip().split("\n")]
def llsv(s):
    return [l.strip() for l in s.strip().split("\n\n")]


#
# Grids
#

def grid(s):
    return [list(l) for l in s.strip().split("\n")]

def igrid(s): 
    return [[int(i) for i in l] for l in s.strip().split("\n")]

# Empty line separated groups
def llsg(s):
    return [[l for l in g.split("\n")] for g in s.strip().split("\n\n")]

#
# Character/digit strings
#

def characters(s):
    return [c for c in list(s.strip())]
def digits(s):
    return [int(d) for d in list(s.strip())]
