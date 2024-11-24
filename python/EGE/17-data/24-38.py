f=open("k7data/k7c-6.txt")
c=f.read()
k,kmax=0,0
for i in range(2,len(c)):
    if len(set([c[i-2],c[i-1],c[i]]))==3:
        k+=1
print(k)
