f=open("k7data/k7-44.txt")
c=f.read()
k,kmax=0,0
for i in c:
    if k>=kmax:
        kmax=k
    if i=='C':
        k+=1
    else:
        k=0
    
print(kmax)
