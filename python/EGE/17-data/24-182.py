f=open('24-181.txt')
s=f.read()
s=s.split('.')
l=[len(m) for m in s]
nmax=0
for i in range(len(l)-2):
    n=l[i]+l[i+1]+l[i+2]
    if n>nmax:
        nmax=n
print(nmax+2)
