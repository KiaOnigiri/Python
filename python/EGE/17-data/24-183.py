f=open('24-181.txt')
s=f.read()
s=s.split('.')
l=[len(m) for m in s]
nmax=0
for i in range(len(l)-3):
    n=l[i]+l[i+1]+l[i+2]+l[i+3]
    if n>nmax:
        nmax=n
print(nmax+3)
