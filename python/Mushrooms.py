n=int(input())
d={}
f={}
for i in range(n-1):
    k,v=input().split()
    f[k]=v
print(f)
a=list(f.keys())
b=list(f.values())
for i in range(len(b)):
    if b[i] not in a:
        continue
    j=a.index(b[i])
    if j>i:
        f1=list(f.items())
        f1=[[k,v] for k,v in f1]
        if a[i] in f1[i] and a[j] in f1[i] and b[i] in f1[j] and b[j] in f1[j]:
            f1[i][0],f1[j][0],f1[i][1],f1[j][1]=f1[j][0],f1[i][0],f1[j][1],f1[i][1]
        f=dict(f1)
print(f)
for k,v in f.items():
    d[v]=d.get(v,0)
    d[k]=d.get(v,0)+1
for k,v in sorted(d.items()):
    print(k,v)
