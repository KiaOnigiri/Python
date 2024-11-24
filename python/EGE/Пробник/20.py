from functools import *
@lru_cache(None)
def game(x):
    if x>=202:
        return 'W'
    if any([game(i)=='W' for i in [x+1,x+4,x*3]]): return 'W1'
    if all([game(i)=='W1' for i in [x+1,x+4,x*3]]): return 'W2'
    if any([game(i)=='W2' for i in [x+1,x+4,x*3]]): return 'W3'
    if all([game(i)=='W1' or game(i)=='W3' for i in [x+1,x+4,x*3]]): return 'W4'


for x in range(1,100):
    if game(x)=='W4':
        print(x)
#67
#63 66
#62
