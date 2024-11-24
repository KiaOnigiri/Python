from functools import *
@lru_cache(None)
def Game(x):
    if x<20:
        return 'W'
    moves=[int(x/3),x-5,x-2]
    if any([Game(m)=='W' for m in moves]): return 'W1'
    if all([Game(m)=='W1' for m in moves]): return 'W2'
    if any([Game(m)=='W2' for m in moves]): return 'W3'
    if all([Game(m)=='W1' or Game(m)=='W3' for m in moves]): return 'W4'

for x in range(20,10000):
    if Game(x)=='W4':
        print(x)
#60
#62 63
#64
