f=open("17-1.txt")
c=f.read().splitlines()
c=[int(z) for z in c]
k=1
mxk=0
g=0
for i in range(len(c)-1):
    if c[i]>c[i+1]:
        k+=1
    if k>=mxk:
        if mxk==k:
            g+=1
        else:
            g=1
            mxk=k
    
    if c[i]<=c[i+1]:
        k=1
print(mxk,g)
