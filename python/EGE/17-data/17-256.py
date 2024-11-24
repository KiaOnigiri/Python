def inAny(x,y):
    b=[]
    while x>0:
        b.append(x%y)
        x//=y
    b.reverse()
    return ''.join([str(z) for z in b])


f=open('17-243.txt')
s=f.read().splitlines()
s=[int(z) for z in s]
k=max([z for z in s if z%107==0])
q=0
fdoj=[]
for i in range(1,len(s)):
    if s[i-1]>k or s[i]>k:
        q+=1
    if '36' in inAny(s[i-1],7) or '36' in inAny(s[i],7):
        q+=1
    if q==2:
        fdoj.append(s[i-1]+s[i])
    q=0
print(len(fdoj),min(fdoj))
