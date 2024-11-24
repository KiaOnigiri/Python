import random
n=6
a=[random.randint(1,5) for x in range(n)]
print(a)
k=1
r=1
for i in range(n-1):
    if a[i] >= a[i+1]:
        k+=1
    if a[i] <= a[i+1]:
        r+=1
    
if k==n:
    print('Убывающий')
elif r==n:
    print('Возрастающий')
else:
    print('Хаотичный')
