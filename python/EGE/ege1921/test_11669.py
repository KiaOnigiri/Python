from functools import *
#from sys import *
#setrecursionlimit(5000)
@lru_cache(None)
def Game(x):
    if x<117:
        return 'W'
    movs=[x-7,int(x/3)]
    if any([Game(m)=='W' for m in movs]): return 'W1'
    if all([Game(m)=='W1' for m in movs]): return 'W2'
    if any([Game(m)=='W2' for m in movs]): return 'W3'
    if all([Game(m)=='W1' or Game(m)=='W3' for m in movs]) and not all([Game(m)=='W1' for m in movs]): return 'W4'
for i in range(10001):
    Game(i)
for S in range(10000,117-1,-1):
    if Game(S)=='W4':
        print(S)
        break
