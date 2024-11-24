f=open('22.txt')
s=f.read().splitlines()
s=s[1:]
s=[[y for y in x.split()] for x in s]
b=[]
for x in s:
    f=[]
    for y in x:
        c=''
        for g in y:
            if g.isdigit():
                c+=g
        f.append(int(c))
    b.append(f)
a=[]
for x in b:
    prcss=x[2:]
    if x[2]==0:
        time=x[1]
        a.append([0+1,time])
    else:
        j=[]
        for y in prcss:
            time=a[y-1][1]+x[1]
            j.append([time-x[1]+1,time])
        a.append(max(j))
r=0
maxtime=max(a, key=lambda x: x[1])[1]
for i in range(1,maxtime+1):
    k=0
    for x in a:
        if x[0]<=i<=x[1]:
            k+=1
    if k==4:
        r+=1
print(r)
