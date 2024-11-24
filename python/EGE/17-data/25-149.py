f=open('24-s2.txt')
#s='AABABAAAAAABABABABABABABABABABAAANAA'
s=f.read()
r=[]
for i in range(1,len(s)-1):
    if s[i-1]=='X' and s[i+1]=='Z':
        r+=s[i]
n=0
nmax=0
l=0
for j in range(len(r)):
    n=r.count(r[j])
    if n>nmax:
        nmax=n
        l=r[j]
print(l,nmax,sep='')
