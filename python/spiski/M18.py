import random
n=5
a=[random.randint(10,99) for x in range (n)]
print(a)
k=0
s=0
b=0
r=0
g=0
for i in range(len(a)):
    b=a[i]
    b=str(b)
    b=list(b)
    b=[int(x) for x in b]
    k=sum(b)
    s+=k
print(s)
