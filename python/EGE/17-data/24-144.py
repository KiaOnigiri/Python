f=open('24-j6.txt')
s=f.read()
k=1
g=0
for i in range(1,len(s)):
    if s[i-1]<s[i]:
        k+=1
    else:
        if k==5:
            g+=1
        k=1
if k==5:
    g+=1
print(g)
    
            
