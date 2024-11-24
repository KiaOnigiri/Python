f=open('24-157.txt')
s=f.read()
k=1
kmax=0
for i in range(1,len(s)):
    if s[i-1]=='Q' and s[i]=='W':
        k=1
    else:
        k+=1
        kmax=max(kmax,k)
print(kmax)
