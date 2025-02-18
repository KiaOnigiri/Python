from functools import *
@lru_cache(None)
def preobr(x,y,z,w):
    if x<6:
        return 0
    if x==6 and y==1 and z==1 and w==0:
        return 1
#    if x==6 and (y==0 or z==0 or w==1):
#        return 0
    if x==19:
        y=1
    if x==29:
        z=1
    if x==24:
        w=1
    return preobr(x-1,y,z,w)+preobr(x-6,y,z,w)+preobr(x//2,y,z,w)
print(preobr(34,0,0,0))
