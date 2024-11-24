from functools import *
@lru_cache(None)
def game(x):
    if 36<=x<=60:
        return 'W'
    if x>60:
        return 'P'
    moves=(x+1,x*2,x*3)
    if any([game(m)=='W' for m in moves]): return 'W1'
    if all([game(m)=='W1' or game(m)=='P' for m in moves]): return 'W2'
    if any([game(m)=='W2' for m in moves]): return 'W3'
    if all([game(m)=='W1' or game(m)=='W3' or game(m)=='P' for m in moves]): return 'W4'


for x in range(1,35+1):
    if game(x)=='W4':
        print(x,game(x))
#34
#1
#11 32
