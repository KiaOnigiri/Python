from functools import *
@lru_cache(None)
def rec(x,y):
    if x==20:
        y=1
    if x==40 and y==1:
        return  1
    if x>40:
        return 0
    return rec(x+2,y)+rec(x*2,y)+rec(x*2+1,y)+rec(x*3,y)+rec(x*3+1,y)+rec(x*3+2,y)


print(rec(4,0))
