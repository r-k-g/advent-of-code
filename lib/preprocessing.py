def I(s):
    return s.strip()
def identity(s):
    return s

#
# Space/comma/line separated values/integers
#

def ssv(s):
    """Space separated strings"""
    return [v.strip() for v in s.strip().split(" ")]
def ssi(s):
    """Space separated integers"""
    return [int(v.strip()) for v in s.strip().split(" ")]
def csv(s):
    """Comma separated strings"""
    return [v.strip() for v in s.strip().split(",")]
def csi(s):
    """Comma separated integers"""
    return [int(v.strip()) for v in s.strip().split(",")]
def lsv(s):
    """Line separated strings"""
    return [l.strip() for l in s.strip().split("\n")]
def lsi(s):
    """Line separated integers"""
    return [int(l.strip()) for l in s.strip().split("\n")]
def llsv(s):
    """Double line separated values"""
    return [l.strip() for l in s.strip().split("\n\n")]


#
# Grids
#

def grid(s):
    """Returns list containing list of every line"""
    return [list(l) for l in s.strip().split("\n")]

def igrid(s): 
    """Grid of integers"""
    return [[int(i) for i in l] for l in s.strip().split("\n")]

# Empty line separated groups
def llsg(s):
    """Empy line separated groups"""
    return [[l for l in g.split("\n")] for g in s.strip().split("\n\n")]

#
# Character/digit strings
#

def characters(s):
    return [c for c in list(s.strip())]
def digits(s):
    return [int(d) for d in list(s.strip())]
