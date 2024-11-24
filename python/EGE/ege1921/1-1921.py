from functools import *
def situats(double):
    x,y=double
    return ((x+1,y),(x*2,y),(x,y+1),(x,y*2))
@lru_cache(None)
def reshenie(double):
    x,y=double
    if (x+y)>=63:
        return 'W'
    if any([reshenie(m)=='W' for m in situats(double)]):
        return 'W1'
    if any([reshenie(m)=='W1' for m in situats(double)]):
        return 'W2'
    if any([reshenie(m)=='W2' for m in situats(double)]):
        return 'W3'
    if all([reshenie(m)=='W1' or reshenie(m)=='W3' for m in situats(double)]):
        return 'W4'


for y in range(1,100+1):
    if reshenie((5,y))=='W4':
        print(y,reshenie((5,y)))
#17
#29 32
#28

#15
#14 27
#25
