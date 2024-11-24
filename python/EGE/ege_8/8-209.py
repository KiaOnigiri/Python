from itertools import *
c='1234567'
a=list(product(c,repeat=9))
k=0
for x in a:
    flag=True
    for y in set(x):
        if x.count(y)>6:
            flag=False
            break
    if flag==True:
        k+=1
            
print(k)
