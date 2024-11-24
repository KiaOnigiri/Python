import random
n=20
a=[random.randint(0,1) for x in range(n)]
print(a)
true=0
k=0
b=[]
for i in range(len(a)):
    if a[i]==true:
        k+=1
    else:
        if k==0:
            b.append(0)
            k+=1
        else:
            b.append(k)
            k=1
        if true==0:
            true=1
        else:
            true=0
if k>0:
    b.append(k)
print(b)
