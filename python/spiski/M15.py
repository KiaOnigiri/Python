import random
n=10
a=[random.randint(10,99) for x in range (n)]
print(a)
for i in range(len(a)):
    if i<5:
        a[i],a[i+5]=a[i+5],a[i]
    else:
        break
print(a)
