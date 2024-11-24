import random
n=10
a=[random.randint(70,99) for x in range(n)]
print(a)
k=9
r=0
for i in range(len(a)):
    if a[i]>k:
        k=a[i]
        r=1
    elif k==a[i]:
        r+=1
print('Max={}, count of max={}'.format(k,r))
