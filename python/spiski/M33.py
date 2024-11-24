import random
n=10
a=[random.randint(1,99) for x in range(n)]
print(a)
for x in range(n):
    for y in range(x+1,len(a)):
        if a[x]*a[y]%15==0:
            print(a[x],a[y])
