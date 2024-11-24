import random
n=15
a=[random.randint(1,5) for x in range (n)]
print(a)
a.reverse()
r=a.index(min(a))
r=r+1
r=r*-1
print(r)
