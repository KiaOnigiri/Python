import random
n=10
a=[random.randint(-99,99) for x in range (n)]
print(a)
for i in range(len(a)):
    if a[i]<0:
        a.pop(i)
        break
a.reverse()
for g in range(len(a)):
    if a[g]<0:
        a.pop(g)
        break
a.reverse()
print(a)
