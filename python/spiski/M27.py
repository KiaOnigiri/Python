import random
n=10
a=[random.randint(10,99) for x in range(n)]
print(*a)
a1=a[:4]
a2=a[-4:]
a1.sort()
a2.sort(reverse=True)
a=a1+a[4:6]+a2
print(a)
