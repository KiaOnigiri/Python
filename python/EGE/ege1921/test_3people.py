from functools import *
def moves(x):
    return (x+1,x*2)
@lru_cache(None)
def game(x):
    if x>=30:
        return 'W'
    if any([game(m)=='W' for m in moves(x)]): return 'W1'
    elif all([game(m)=='W1' for m in moves(x)]): return 'W2'
    elif any([game(m)=='W2' for m in moves(x)]): return 'W3'
    else:
        game(x+1)
        game(x*2)


for i in range(1,29+1):
    if game(i)=='W3':
        print(i,game(i))
