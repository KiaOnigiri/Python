def sopryag(g):
    b=[]
    t=sum([int(j) for j in str(g)])
    if g%2==0:
        h=2
    else:
        h=1
    for i in range(h,10,2):
        if t>=10:
            b.append(int(str(i)+str(t)))
        else:
            b.append(int(str(i)+'0'+str(t)))
    return b


x,y=input().split()
x,y=int(x),int(y)
m,n=input().split()
m,n=int(m),int(n)
l=[]
r=[]
for p in sopryag(x):
    if m<=p<=n:
        l.append(p)
for o in sopryag(y):
    if m<=o<=n:
        r.append(o)
lr=list(set(l+r))
print(len(lr))
if len(lr)!=0:
    if min(l)<=min(r):
        v='L'
        z=min(l)
    else:
        v='R'
        z=min(r)
    print(v+str(z))
