from functools import *
@lru_cache(None)
def game(x):
    if x<10:
        return 'W'
    moves=[x-1]
    if x%2==0:
        moves=moves+[x//2]
    if x%3==0:
        moves=moves+[2*x//3]
    if any([game(m)=='W' for m in moves]): return 'W1'
    if all([game(m)=='W1' for m in moves]): return 'W2'
    if any([game(m)=='W2' for m in moves]): return 'W3'
    if all([game(m)=='W1' or game(m)=='W3' for m in moves]): return 'W4'

for s in range(60,10-1,-1):
    if game(s)=='W4':
        print(s,game(s))
print(game(21),game(14),game(20))
#27 - W1
#19 - W2
#34 38 - W3
#23 - W4
