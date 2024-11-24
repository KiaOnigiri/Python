def tri(s):
    c=''
    for x in s:
        c+=x
        if len(set(c))==4:
            c=c[:-1]
            return c
    return c


f=open('24-168.txt')
s=f.read()
b=[]
k=0
kmax=0
l=[]
g=0
for i in range(1,len(s)):
    if s[i-1]<=s[i]:
        if g==0:
            l.append(s[i-1])
        l.append(s[i])
        g+=1
    else:
        b.append(l)
        l=[]
        g=0
h=0
for j in b:
    if len(set(j))==3:
        k=len(j)
        kmax=max(kmax,k)
    elif len(set(j))<3:
        k=len(j)
        kmax=max(kmax,k)
    elif len(set(j))>3:
        while len(set(j))!=3:
            k=tri(j)
            kmax=max(kmax,len(k))
            x=0
            h=j[x]
            n=j[x]
            while h==n:
                j.remove(n)
                h=j[x]
            
print(kmax)
