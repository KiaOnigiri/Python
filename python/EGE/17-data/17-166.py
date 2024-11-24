f=open("17-3.txt")
c=f.read().splitlines()
c=[int(z) for z in c]
b=[]
for i in range(1,len(c)-1):
    if c[i-1]<c[i]<c[i+1]:
        b.append([c[i-1],c[i],c[i+1]])
l=[]
for j in range(len(b)):
                 l.append(b[j][2]-b[j][0])
print(len(b),min(l))
