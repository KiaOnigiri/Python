import random
n=10
a=[random.randint(-99,99) for x in range (n)]
print(a)
b=[]
for i in range(len(a)):
    if a[i]>=0:
        b.append(a[i])
a=b
print(a)
