f=open('24-4.txt')
s=f.read()
k=1
kmax=0
imax=0
for i in range(1,len(s)):
    if s[i-1]<s[i]:
        k+=1
        if k>kmax:
            kmax=k
            imax=i
    else:
        k=1
        
print(kmax,s[imax-kmax+1:imax+1])
