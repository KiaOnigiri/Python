from sys import *
from functools import *

#@lru_cache(None)
setrecursionlimit(100000)
def recurs(x,y):
    ans=[recurs(x+1,y+1),recurs(x-1,y+1)]
    if y!=7 and x==5:
        return None
    if y==7 and x==5:
        return 1
    if y>7:
        return None

print(recurs(0,0))

'''
k=0
for tri in range(1,676):
    for pat in range(1,406):
        if 3*tri+5*pat==2023:
            k+=1
print(k)
'''
