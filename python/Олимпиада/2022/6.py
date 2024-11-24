from itertools import permutations
from math import *
n=int(input())
x=int(input())
y=int(input())
a=[]
d=1

for n in range(n):
    a.append(int(input()))
mn=1
if y-min(a)>x:
    print(0)
elif sum(a)<y*n:
    print(0)
else:
    m=list([x for x in permutations(a)])
    k=0
    for i in range(len(m)):
        sklad=0
        for j in range(len(m[i])):
            sklad+=y
            zab=m[i][j]
            if zab>sklad:
                zab=sklad
            sklad-=zab
            if sklad>x:
                break
        if sklad==0:
            k+=1
    print(k)
