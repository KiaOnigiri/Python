import random
n=10
a=[random.randint(10,20) for p in range(n)]
print(a)
x=int(input('x='))
b=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==x:
            b+=['II',a[i],a[j]]
print(b)
