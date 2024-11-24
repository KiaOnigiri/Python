def sosedi(a):
    b=[]
    for i in range(len(a)-1):
        if a[i+1]-a[i]==1:
            if ((a[i]-1) not in a and a[i]-2 in a):
               b.append(a[i]-1)
            if ((a[i+1]+1) not in a and a[i+1]+2 in a):
                b.append(a[i+1]+1)
            if a[i]-1 in a and a[i]-2 not in a:
                b.append(a[i]-2)
            if a[i+1]+1 in a and a[i+1]+2 not in a:
                b.append(a[i+1]+2)
    return sorted(set(b))

f=open('26-93.txt')
s=f.read().splitlines()
n,m=s[0].split()
n=int(n)
m=int(m)
s=s[1:]
s=[[int(x) for x in z.split()] for z in s]
s.sort()
d=dict()
for flat in s:
    if d.get(flat[0]):
        d[flat[0]].append(flat[1])
    else:
        d[flat[0]]=[flat[1]]
ans1=0
ans2=0
for k,v in d.items():
    q=sosedi(v)
    #if len(v)>=3:
    #    print(k,q,v)
    if len(q)>0:
        #print(k,q,v)
        ans1+=len(q)
        ans2=k
print(ans1)
print(ans2)
    
