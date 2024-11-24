def sopryag(N):
    s=[]
    sm=sum([int(z) for z in str(N)])
    for M in range(100,999+1):
        if N%2==0 and int(str(M)[0])%2!=0:
            continue
        if N%2!=0 and int(str(M)[0])%2==0:
            continue
        if int(str(M)[-2:])==sm:
            s.append(M)
    return s
            
        
      
    


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

if not l and not r:
    print(0)
elif l and r:
    print('R'+str(max(l+r)))
elif l:
    print('L'+str(max(l)))
elif r:
    print('R'+str(max(r)))
