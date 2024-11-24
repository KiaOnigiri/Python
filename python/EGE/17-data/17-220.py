f=open("17-1.txt")
c=f.read().splitlines()
c=[int(z) for z in c]
s=sum(c)/len(c)
b=[]
for i in range(len(c)-1):
    if (c[i]>s and c[i+1]<s) or (c[i+1]>s and c[i]<s):
        b.append(c[i]+c[i+1])
print(len(b),max(b))
