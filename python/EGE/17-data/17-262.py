f=open("17-257.txt")
c=f.read().splitlines()
c=[int(z) for z in c]
k=10000
b=0
l=[]
for j in range(len(c)):
    if c[j]%2!=0 and c[j]<k:
        k=c[j]
for r in range(len(c)):
    if c[r]%2!=0 and c[r]>b:
        b=c[r]
for i in range(1,len(c)):
    if (c[i-1]+c[i])%2==0 and (c[i-1]+c[i])>(b+k):
        l.append(c[i-1]+c[i])
print(len(l),min(l))
