f=open("k7data/k7a-5.txt")
c=f.read()
k,kmax=0,0
for i in c:
    if i not in 'CF':
        k+=1
    else:
        k=0
    if k>=kmax:
        kmax=k
    
print(kmax)
