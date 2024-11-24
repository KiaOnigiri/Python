f=open('05')
s=f.read().splitlines()
n,m=map(int, s[0].split())
f.close()
a=list(map(int, s[1].split()))
print(a)
c=s[2:]
b=[]
print('-----')
for i in range(len(c)):
    si=c[i].split()
    if si[0]=='1':
        for j in range(len(a)):
            a[j]+=1
    if si[0]=='2':
        a.append(int(si[1]))
    if si[0]=='3' and int(si[1]) in a:
        a.remove(int(si[1]))
    #print(a)
    m=a[0]
    for j in range(1,len(a)):
        m=m^a[j]
    b.append(m)
#print('-----')
print(b)
