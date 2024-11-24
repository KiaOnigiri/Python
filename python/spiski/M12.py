import random
n=10
a=[random.randint(10,20) for x in range (n)]
print(a)
k=0
a.reverse()
k=a.index(min(a))
k+=1
k*=-1
print(k)
a.reverse()
for i in range(len(a)):
    a[k],a[a.index(max(a))]=a[a.index(max(a))],a[k]
    break
print(a)

