f=open('k8data\k8-7.txt')
s=f.read()
k=1
kmax=0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        k+=1
        kmax=max(kmax,k)
    else:
        k=1
print(kmax)
