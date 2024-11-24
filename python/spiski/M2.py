import random
n=10
a=[random.randrange(-99,99) for x in range (n)]
print(a)
for i in range(len(a)):
    if a[i]<0 and a[i]%2==0:
        print(a[i])
