from time import time
from functools import *
@lru_cache(None)
def f(x):
    if x==0:
        return 1
    elif x%2!=0:
        return (x%10)*f(x//100)
    elif x>0 and x%2==0:
        return f(x//100)

t1=time()
n=0
for k in range(10_000_000,8*10_000_000+1):
    if k%1000000==0:
        print(k,'!')
    '''k=str(k)
    k=list(reversed(k))
    m=1
    for x in k:
        if int(x)%2!=0:
            m*=int(x)'''
    m=f(k)
    if m==35:
        n+=1
        #print(k)
        #if n==5:
        #    break
        
print(n)
t2=time()
print(t2-t1)
