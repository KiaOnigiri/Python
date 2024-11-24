import random
n=10
a=[random.randint(10,30) for x in range(n)]
print(*a)
k=min(a)
for i in range(len(a)):
    a[i]/=k
print('Min = {}'.format(k))
print(*a)
