f=open('24-181.txt')
s=f.read()
s=s.split('.')
l=[len(m) for m in s]
nmax=0
for i in range(len(l)-1):
    n=l[i]+l[i+1]
    if n>nmax:
        nmax=n
        print(l[i],l[i+1],n)
print(nmax)
