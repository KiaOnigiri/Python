from functools import *
def moves(x):
    return [x+1,x*2]
@lru_cache(None)
def game(x):
    if x>=129:
        return 'W'
    if any([game(m)=='W' for m in moves(x)]):
        return 'W1'
    if all([game(m)=='W1' for m in moves(x)]):
        return 'W2'
    if any([game(m)=='W2' for m in moves(x)]):
        return 'W3'
    if all([game(m)=='W1' or game(m)=='W3' for m in moves(x)]):
        return 'W4'


for s in range(1,128+1):
    if game(s)=='W4':
        print(s)
#64
#32 63   
#62
