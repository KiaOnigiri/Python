from functools import *



def moves(x):
    n1=x-2
    n2=x-3
    if x%3==0:
        n1=x//3
    if x%5==0:
        n2=x//5
    return [x-1,n1,n2]

@lru_cache(None)
def Game(x):
    if x<=19:
        return 'W'
    if any([Game(i)=='W' for i in moves(x)]):return 'W1'
    if all([Game(i)=='W1' for i in moves(x)]):return 'W2'
    if any([Game(i)=='W2' for i in moves(x)]):return 'W3'
    if all([Game(i)=='W1' or Game(i)=='W3' for i in moves(x)]):return 'W4'



for s in range(20,150):
    if Game(s)=='W4':
        print(s)
#23
#26 69
#
