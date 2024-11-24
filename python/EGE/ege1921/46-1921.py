from functools import *
from sys import *
def moves(x):
    return (x+2,x*3)
@lru_cache(None)
def game(x):
    if x>=45 and x<=112:
        return 'W'
    if x>112:
        return 'perebor'
    if any([game(m)=='W' for m in moves(x)]): return 'W1'
    if all([game(m)=='W1' or game(m)=='perebor' for m in moves(x)]): return 'W2'
    if any([game(m)=='W2' for m in moves(x)]): return 'W3'
    if all([game(m)=='W1' or game(m)=='W3' or game(m)=='perebor' for m in moves(x)]): return 'W4'


setrecursionlimit(10000)
for x in range(1,45):
    if game(x)=='W2':
        print(x,game(x))
#41
#3
#12 38
