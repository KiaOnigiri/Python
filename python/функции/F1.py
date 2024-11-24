def extrems(x):
    k=min(x)
    m=max(x)
    r=x.count(k)
    h=x.count(m)
    return k,m,r,h


import random
n=20
a=[random.randint(10,20) for x in range(n)]
print(a)
print(extrems(a))
