from functools import *
def moves(x, prev):
    m=[[x+1,0],[x+2,1],[x*2,2]]
    if prev!=-1:
        m.pop(prev)
    return m
@lru_cache(None)
def game(x, prev):
    if x>=43: return 'W'
    if any([game(i,j)=='W' for i,j in moves(x,prev)]): return 'W1'
    if all([game(i,j)=='W1' for i,j in moves(x,prev)]): return 'W2'
    if any([game(i,j)=='W2' for i,j in moves(x,prev)]): return 'W3'
    if all([game(i,j)=='W3' or game(i,j)=='W1' for i,j in moves(x,prev)]): return 'W4'
    

for x in range(1,43):
    gm=game(x,-1)
    if gm=='W4':
        print(gm,x)
#21
#11 20
#10
