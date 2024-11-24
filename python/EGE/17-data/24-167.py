def maxsame(s):
    kmax=0
    for i in range(len(s)):
        a=s[i]
        p=s.rfind(a)
        r=p-i+1
        if r>kmax:
            kmax=r
    return kmax


f=open('24-164.txt')
s=f.read().splitlines()
k=0
kmax=0
for i in range(len(s)):
    if s[i].count('E')<20:
        k=maxsame(s[i])
        if k>kmax:
            kmax=k
print(kmax)
