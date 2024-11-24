import random
n=20
a=[random.randint(0,1) for x in range(n)]
print(a)
k=0
kmax=0
kadr=0
for i in range(n):
    if a[i]==0:
        k+=1
        if kmax<k:
            kadr=i
            kmax=k        
    else:
        k=0
print(kmax,kadr-kmax+1)
