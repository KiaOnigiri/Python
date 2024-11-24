import random
n=10
a=[random.randint(10,99) for x in range (n)]
print(a)
k=0
t=0
k=sum(a)/n
for it in range(len(a)):
    if k<=a[it]:
        t+=1
print(k)
print('Больше или равно среднему арифметическому: '+str(t))
