import random
n=20
a=[random.randint(10,30) for i in range(n)]
print(*a)
k=31
ik=0
for i in range(len(a)):
    if a[i]<k:
        k=a[i]
        ik=i
a.pop(ik)
r=31
for j in range(len(a)):
    if a[j]<r:
        r=a[j]
print(k,r)
