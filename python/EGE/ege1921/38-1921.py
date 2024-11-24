from functools import *
def moves(x):
    b=[x*3,x+1,x+3]
    b=[j for j in b if j%2!=0]
    return b
@lru_cache(None)
def game(x):
    if x>=51:
        return 'W'
    mov=moves(x)
    if any([game(m)=='W' for m in mov]): return 'W1'
    if all([game(m)=='W1' for m in mov]): return 'W2'
    if any([game(m)=='W2' for m in mov]): return 'W3'
    if all([game(m)=='W3' for m in mov]): return 'W4'
for i in range(1,50+1):
    if game(i)=='W4':
        print(i,game(i))
#7
#12 14
