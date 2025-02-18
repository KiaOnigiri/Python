from functools import *
@lru_cache(None)
def game(x):
    if x>=132:
        return 'W'
    moves=(x+3,x+6,x*3)
    if any([game(y)=='W' for y in moves]): return 'W1'
    if all([game(y)=='W1' for y in moves]): return 'W2'
    if any([game(y)=='W2' for y in moves]): return 'W3'
    if all([game(y)=='W1' or game(y)=='W3' for y in moves]): return 'W4'
for S in range(1,131+1):
    if game(S)=='W4':
        print(S)
