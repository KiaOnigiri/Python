from functools import *
@lru_cache(None)
def ege23(x,y,c):
    print(x,y,c)
    if x-1>y or (x==y+1 and c==1):
        return 0
    if x==y:
        return 1
    if x==y+1 and c!=1:
        return ege23(x-1,y,1)
    if x<y and c==1:
        return ege23(x+3,y,2)+ege23(x*2,y,3)
    if x<y and c!=1:
        return ege23(x-1,y,1)+ege23(x+3,y,2)+ege23(x*2,y,3)


print(ege23(3,12,2))
#53
