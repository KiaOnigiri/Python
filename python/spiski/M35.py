import random
n=8
a=[random.randint(0,6) for x in range(n-2)]
print(a)
k=0
b=[]
for i in range(len(a)):
    for j in range(a[i]):
        if k==0:
            b.append(0)
        elif k==1:
            b.append(1)
    if k==0:
        k=1
    elif k==1:
        k=0
print(b)
