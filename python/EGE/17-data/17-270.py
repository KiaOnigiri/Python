f=open("17-243.txt")
c=f.read().splitlines()
c=[int(z) for z in c]
b=[]
l=0
for j in range(len(c)):
    g=[int(z) for z in str(c[j])]
    if c[j]%35==0:
        print(c[j])
        l+=sum(g)
print('sum=',l)
for i in range(1,len(c)):
    if (c[i-1]>l and c[i]<=l and hex(c[i])[-2:]=='ef') or (c[i-1]<=l and c[i]>l and hex(c[i-1])[-2:]=='ef'):
        b.append(c[i-1]+c[i])
print(b)
print(len(b),min(b))
