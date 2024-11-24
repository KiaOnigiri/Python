import random
n=15
a=[random.randint(10,20) for x in range (n)]
print(a)
k=0
for i in range(len(a)):
    if max(a)==a[i]:
        k+=1
print(max(a))
print('-----------------------------')
print(k)
print('-----------------------------')
for i in range(len(a)):
    if max(a)==a[i]:
        print(i)
