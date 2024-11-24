f=open('26-86.txt')
s=f.read().splitlines()
n=int(s[0])
s=s[1:]
s=[[int(x) for x in z.split()]for z in s]
s.sort()
d=dict()
for x in s:
    if d.get(x[1]):
        d[x[1]].append(x[0])
    else:
        d[x[1]]=[x[0]]
print(d[0])
kmax=0
for i in range(0,1000):
    k=0
    for t,v in d.items():
        for j in range(1,len(v),2):
            if i<=v[j]<i+60:
                k+=1
    kmax=max(kmax,k)
    k=0
print(kmax)
'''
k=0
kmax=0
for i in range(0,960-60+1):
    k=0
    a,b=i,i+60
    for k,v in d.items():
        for ends in range(1,len(d[k]),2):
            if a<=ends<=b:
                k+=1
    if k>kmax:
        kmax=k
print(kmax)
'''
g=dict()
for k,v in d.items():
    cnt=len(v)//2
    sm=0
    for t in range(1,len(d[k]),2):
        sm+=d[k][t]-d[k][t-1]
    if cnt!=0:
        g[k]=sm/cnt
print(d[139])
print(sorted(g.items(),key=lambda x: x[1],reverse=True)[0])
