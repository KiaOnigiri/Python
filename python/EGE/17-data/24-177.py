f=open('24-157.txt')
s=f.read()
k=1
kmax=0
for i in range(1,len(s)):
    if s[i-1]=='P' and s[i]=='R' or s[i-1]=='R' and s[i]=='P':
        k=1
    else:
        k+=1
        kmax=max(kmax,k)
print(kmax)
