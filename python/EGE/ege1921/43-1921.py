from functools import *
def moves(x):
    return (x+1,x+2,x+3,x*2)
@lru_cache(None)
def game(x):
    if x>=34:
        return 'W'
    if any([game(m)=='W' for m in moves(x)]): return 'W1'
    if all([game(m)=='W1' for m in moves(x)]): return 'W2'
    if any([game(m)=='W2' for m in moves(x)]): return 'W3'
    if all([game(m)=='W1' or game(m)=='W3' for m in moves(x)]): return 'W4'
    


for i in range(1,33+1):
    if game(i)=='W4':
        print(i,game(i))
#16
#8 15
#12
