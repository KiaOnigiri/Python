from functools import *
from sys import *
def moves(x):
    return (x+1,x*2)
@lru_cache(None)
def game(x):
    if x>=50 and x<=70:
        return 'W'
    if x>70:
        return 'perebor'
    if any([game(m)=='W' for m in moves(x)]): return 'W1'
    if all([game(m)=='W1' or game(m)=='perebor' for m in moves(x)]): return 'W2'
    if any([game(m)=='W2' for m in moves(x)]): return 'W3'
    if all([game(m)=='W1' or game(m)=='W3' or game(m)=='perebor' for m in moves(x)]): return 'W4'


setrecursionlimit(10000)
for x in range(1,50):
    if game(x)=='W4':
        print(x,game(x))
#13
#24 47
#46
