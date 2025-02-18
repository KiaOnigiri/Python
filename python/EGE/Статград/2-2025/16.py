from functools import *

@lru_cache(None)
def F(n):
    if n%2==0:
        return F(n/2)+3
    elif n%3==0:
        return F(n/3)+2
    else:
        return 0

for n in range(37748736,37748736+1):
    print(n,F(n))
#22*3 + 2*2
#37748736
