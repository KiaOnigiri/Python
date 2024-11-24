f=open('26-76.txt')
s=f.read().splitlines()
l,m=[int(z) for z in s[0].split()]
s=s[1:]
s=[[int(q) for q in z.split()] for z in s]
s.sort()
print(s[:50])
a=[0]*150301
for x in s:
    for i in range(x[0],x[1]+1):
        a[i]=1
b=[]
k=0
for g in a:
    if g==0:
        k+=1
    elif k>0:
        b.append(k)
        k=0
if k>0:
    b.append(k)
print(m)
print(b)
ans1=len([j for j in b if j>=m])
ans2=max(b)
print(ans1,ans2)
