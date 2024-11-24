import random
n=5
a=[9,7,7,9,9,8,8]
#a=[random.randint(10,25) for x in range (n)]
print(a)
k=0
r=0
for i in range (len(a)):
    if a.count(a[i])>k:
        k+=1
        r=a[i]
print(k,r)
