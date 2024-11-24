f=open("17-1.txt")
c=f.read().splitlines()
c=[int(z) for z in c]
b=[]
for i in range(1,len(c)-1):
    if c[i-1]<c[i]>c[i+1]:
        b.append(i)
mn=len(c)
for j in range(1,len(b)):
    r=abs(b[j-1]-b[j])
    if r<mn:
        mn=r
print(len(b),mn)
