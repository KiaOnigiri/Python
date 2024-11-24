import random
n=5
a=[random.randint(10,99) for x in range (n)]
print(a)
for i in range(n//2):
    a[i],a[-1-i]=a[-1-i],a[i]
print(a)
