f=open('k8data/k8-4.txt')
s=f.read()
k=1
kmax=0
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        k+=1
        if k==4:
            print(s[i],' ',4)
    else:
        k=1

