import random
n=10
a=[random.randint(10,99) for x in range (n)]
print(a)
k=9
for i in range(len(a)):
    if i%2==0 and a[i]>k:
        k=a[i]
print(k)
