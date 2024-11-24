from functools import *
def moves(x):
    return [x+100,x*2]
@lru_cache(None)
def game(x):
    if x>=1000:
        return 'W'
    mov=moves(x)
    if any([game(m)=='W' for m in mov]): return 'W1'
    if all([game(m)=='W1' for m in mov]): return 'W2'
    if any([game(m)=='W2' for m in mov]): return 'W3'
    if all([game(m)=='W3' or game(m)=='W1' for m in mov]) and any([game(m)=='W1' for m in mov]): return 'W4'
k=0
for i in range(1,999+1):
    if game(i)=='W4':
        k+=1
        print(i,game(i))
#100
#150
#100 299
