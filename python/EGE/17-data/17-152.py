f=open("17-1.txt")
c=f.read().splitlines()
c=[int(z) for z in c]
b=[]
for i in range(len(c)-1):
    if (c[i]%9!=0 and c[i]%8==3 and c[i+1]%9==0) or (c[i+1]%9!=0 and c[i]%9==0 and c[i+1]%8==3):
        b.append([c[i],c[i+1]])
c=[]
for j in range(len(b)):
    c.append(max(b[j]))
print(len(b),max(c))
