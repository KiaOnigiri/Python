f=open("17-1.txt")
c=f.read().splitlines()
c=[int(z) for z in c]
b=[]
for i in range(1,len(c)):
    if c[i-1]<c[i]:
        b.append([c[i-1],c[i]])
c=[]
for j in range(len(b)):
    c.append(abs(b[j][0]-b[j][1]))
print(len(b),min(c))
