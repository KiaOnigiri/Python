from functools import *
@lru_cache(None)
def game(x,y):
    if x+y>=79:
        return 'W'
    moves=[[x,y+3],[x,y*2],[x+3,y],[x*2,y]]
    if any([game(i,j)=='W' for i,j in moves]): return 'W1'
    if all([game(i,j)=='W1' for i,j in moves]): return 'W2'
    if any([game(i,j)=='W2' for i,j in moves]): return 'W3'
    if all([game(i,j)=='W3' or game(i,j)=='W1' for i,j in moves]): return 'W4'


for x in range(1,69+1):
    gm=game(x,9)
    if gm=='W4':
        print(x,gm)
#18
#17
#26 27
