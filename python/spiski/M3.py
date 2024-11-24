import random
x=int(input())
n=10
a=[random.randrange(0,9) for x in range (n)]
print(a)
k=0
for i in range(len(a)):
    if a[i]==x:
        k+=1
print(k, k*x)
