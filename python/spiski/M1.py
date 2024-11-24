import random
n=10
a=[random.randrange(10,99) for x in range (n)]
print(a)
for i in range(len(a)):
    if a.index(a[i])%2==0:
        print(a[i], end=' ')
print(' ')
for i in range(len(a)):
    if a.index(a[i])%2!=0:
        print(a[i], end=' ')
