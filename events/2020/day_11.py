import random, os, sys, re, statistics
from collections import deque, OrderedDict, Counter
from itertools import chain, combinations
from functools import lru_cache
from copy import deepcopy

class SeatMap:
    def __init__(self, plot):
        self.plot = plot
        self.rowlen = len(plot)
        self.collen = len(plot[0])
    
    def fillseats(self):
        while True:
            origplot = deepcopy(self.plot)

            for row in range(self.rowlen):
                for col in range(self.collen):
                    if origplot[row][col] == '.':
                        pass 

                    elif origplot[row][col] == 'L':

                        occupied = False

                        if not row == 0: # up
                            r  = row - 1
                            while True:
                                if r < 0:
                                    break
                                try:
                                    if origplot[r][col] == 'L':
                                        break
                                    elif origplot[r][col] == '#':
                                        occupied = True
                                        break
                                except IndexError:
                                    break
                                r -= 1

                        if (not row == 0) and (not col == self.collen - 1): # diag right up
                            r, c = row - 1, col + 1
                            while True:
                                if r < 0 or c < 0:
                                    break
                                try:
                                    if origplot[r][c] == 'L':
                                        break
                                    elif origplot[r][c] == '#':
                                        occupied = True
                                        break
                                except IndexError:
                                    break
                                r -= 1
                                c += 1
                        
                        if not col == self.collen - 1: # right
                            c = col + 1
                            while True:
                                if c < 0:
                                    break
                                try:
                                    if origplot[row][c] == 'L':
                                        break
                                    elif origplot[row][c] == '#':
                                        occupied = True
                                        break
                                except IndexError:
                                    break
                                c += 1
                        
                        if (not row == self.rowlen-1) and (not col == self.collen - 1): # diag right down
                            r, c = row + 1, col + 1
                            while True:
                                if r < 0 or c < 0:
                                    break
                                try:
                                    if origplot[r][c] == 'L':
                                        break
                                    elif origplot[r][c] == '#':
                                        occupied = True
                                        break
                                except IndexError:
                                    break
                                r += 1
                                c += 1
                        
                        if not row == self.rowlen - 1: # down
                            r  = row + 1
                            while True:
                                if r < 0:
                                    break
                                try:
                                    if origplot[r][col] == 'L':
                                        break
                                    elif origplot[r][col] == '#':
                                        occupied = True
                                        break
                                except IndexError:
                                    break
                                r += 1
                        
                        if (not row == self.rowlen-1) and (not col == 0): # diag left down
                            r, c = row + 1, col -1
                            while True:
                                if r < 0 or c < 0:
                                    break
                                try:
                                    if origplot[r][c] == 'L':
                                        break
                                    elif origplot[r][c] == '#':
                                        occupied = True
                                        break
                                except IndexError:
                                    break
                                r += 1
                                c -= 1
                        
                        if not col == 0: # left
                            c = col - 1
                            while True:
                                if c < 0:
                                    break
                                try:
                                    if origplot[row][c] == 'L':
                                        break
                                    elif origplot[row][c] == '#':
                                        occupied = True
                                        break
                                except IndexError:
                                    break
                                c -= 1

                        if (not row == 0) and (not col == 0): # diag left up
                            r, c = row - 1, col - 1
                            while True:
                                if r < 0 or c < 0:
                                    break
                                try:
                                    if origplot[r][c] == 'L':
                                        break
                                    elif origplot[r][c] == '#':
                                        occupied = True
                                        break
                                except IndexError:
                                    break
                                r -= 1
                                c -= 1

                        if not occupied:
                            rowsplit = list(self.plot[row])
                            rowsplit[col] = '#'
                            self.plot[row] = ''.join(rowsplit)

                    elif origplot[row][col] == '#':
                        occupied = 0

                        if not row == 0: # up
                            r  = row - 1
                            while True:
                                if r < 0:
                                    break
                                try:
                                    if origplot[r][col] == 'L':
                                        break
                                    elif origplot[r][col] == '#':
                                        occupied += 1
                                        break
                                except IndexError:
                                    break
                                r -= 1

                        if (not row == 0) and (not col == self.collen - 1): # diag right up
                            r, c = row - 1, col + 1
                            while True:
                                if r < 0 or c < 0:
                                    break
                                try:
                                    if origplot[r][c] == 'L':
                                        break
                                    elif origplot[r][c] == '#':
                                        occupied += 1
                                        break
                                except IndexError:
                                    break
                                r -= 1
                                c += 1
                        
                        if not col == self.collen - 1: # right
                            c = col + 1
                            while True:
                                if c < 0:
                                    break
                                try:
                                    if origplot[row][c] == 'L':
                                        break
                                    elif origplot[row][c] == '#':
                                        occupied += 1
                                        break
                                except IndexError:
                                    break
                                c += 1
                        
                        if (not row == self.rowlen-1) and (not col == self.collen - 1): # diag right down
                            r, c = row + 1, col + 1
                            while True:
                                if r < 0 or c < 0:
                                    break
                                try:
                                    if origplot[r][c] == 'L':
                                        break
                                    elif origplot[r][c] == '#':
                                        occupied += 1
                                        break
                                except IndexError:
                                    break
                                r += 1
                                c += 1
                        
                        if not row == self.rowlen - 1: # down
                            r  = row + 1
                            while True:
                                if r < 0:
                                    break
                                try:
                                    if origplot[r][col] == 'L':
                                        break
                                    elif origplot[r][col] == '#':
                                        occupied += 1
                                        break
                                except IndexError:
                                    break
                                r += 1
                        
                        if (not row == self.rowlen-1) and (not col == 0): # diag left down
                            r, c = row + 1, col -1
                            while True:
                                if r < 0 or c < 0:
                                    break
                                try:
                                    if origplot[r][c] == 'L':
                                        break
                                    elif origplot[r][c] == '#':
                                        occupied += 1
                                        break
                                except IndexError:
                                    break
                                r += 1
                                c -= 1
                        
                        if not col == 0: # left
                            c = col - 1
                            while True:
                                if c < 0:
                                    break
                                try:
                                    if origplot[row][c] == 'L':
                                        break
                                    elif origplot[row][c] == '#':
                                        occupied += 1
                                        break
                                except IndexError:
                                    break
                                c -= 1

                        if (not row == 0) and (not col == 0): # diag left up
                            r, c = row - 1, col - 1
                            while True:
                                if r < 0 or c < 0:
                                    break
                                try:
                                    if origplot[r][c] == 'L':
                                        break
                                    elif origplot[r][c] == '#':
                                        occupied += 1
                                        break
                                except IndexError:
                                    break
                                r -= 1
                                c -= 1

                        if occupied >= 5:
                            rowsplit = list(self.plot[row])
                            rowsplit[col] = 'L'
                            self.plot[row] = ''.join(rowsplit)

            if self.plot == origplot:
                print(self.countoccupied())
                break

    def countoccupied(self):
        occ = 0
        for row in self.plot:
            for item in row:
                if item == '#':
                    occ += 1
        return occ

with open('day_11_inp.txt', 'r') as inp:
    result = inp.read().split('\n')

sm = SeatMap(result)
sm.fillseats()