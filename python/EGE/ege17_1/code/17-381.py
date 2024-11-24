f=open('../17-381.txt')
s=f.read().splitlines()
s=[int(y) for y in s]
print(s[:10])
mx=max([x for x in s if len(str(x))==4 and str(x)[-2:]=='39'])
print(mx)
b=[]
for i in range(len(s)-1):
    g1=abs(s[i])
    g2=abs(s[i+1])
    if (1000<=g1<=9999 and len(str(g2))!=4) or (1000<=g2<=9999 and len(str(g1))!=4):
        if (s[i]+s[i+1])**2<=mx**2:
            b.append(s[i]+s[i+1])
print(len(b),max(b))
