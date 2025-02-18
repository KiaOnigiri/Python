from functools import *
def moves(x):
    b=[x-5]
    if x%2==0:
        b.append(x//2)
    if x%3==0:
        b.append(x//3)
    if x%2!=0 and x%3!=0:
        b.append(x+1)
    return b

@lru_cache(None)
def game(x):
    if x<=19:
        return 'W'
    if any(game(y)=='W' for y in moves(x)): return 'W1'
    if all(game(y)=='W1' for y in moves(x)): return 'W2'
    if any(game(y)=='W2' for y in moves(x)): return 'W3'
    if all(game(y)=='W1' or game(y)=='W3' for y in moves(x)): return 'W4'
    
for S in range(20,100):
    if game(S)=='W4':
        print(S,game(S))

#25
#40 43
#60
