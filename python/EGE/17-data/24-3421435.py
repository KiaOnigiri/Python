f=open('k8data\k8-0.txt')
s=f.read()
k=1
b=0
kmax=0

for i in range(len(s)-1):
    if s[i]==s[i+1]:
        k+=1
        if k==3:
            kmax=k
            b=s[i]
    else:
        k=1
print(b,' ',kmax)
