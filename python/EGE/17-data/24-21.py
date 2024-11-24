f=open("k7data/k7a-1.txt")
c=f.read()
k,kmax=0,0
for i in c:
    if i in 'ABC':
        k+=1
    else:
        k=0
    if k>=kmax:
        kmax=k
    
print(kmax)
