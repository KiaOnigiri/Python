import random
n=20
a=[random.randint(-99,20) for x in range (n)]
print(a)
k=21
for i in range(len(a)):
    if a[i]>0 and a[i]%5==0 and k>a[i]:
        k=a[i]
if k==21:
    print('Такого нет')
else:
    print(k)
