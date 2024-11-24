import time
t1=time.time()
f=open('24-s2.txt')
#s='AABABAAAAAABABABABABABABABABABAAANAA'
s=f.read()
r=[]
for i in range(1,len(s)):
    if s[i-1]=='A':
        r+=s[i]
n=0
nmax=0
l=0
ur=list(set(r))
for j in range(len(ur)):
    n=r.count(ur[j])
    if n>nmax:
        nmax=n
        l=ur[j]
print(l,nmax,sep='')
t2=time.time()
print(t2-t1)
