import random
n=10
a=[random.randint(10,30) for x in range(n)]
print(*a)
a1=a[:n//2]
a2=a[n//2:]
a1.reverse()
a2.reverse()
print(*a1,*a2)
