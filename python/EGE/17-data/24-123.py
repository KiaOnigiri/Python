f=open('24-1.txt')
s=f.read()
k=0
r=0
mx=0
h=0
g=0
for i in range(1,len(s)-1):
    if s[i-1]<s[i]>s[i+1] and g==0:
        k=i
        if k!=0 and r!=0:
            h=abs(r-k)
    if s[i-1]<s[i]>s[i+1] and g==1:
        r=i
        if k!=0 and r!=0:
            h=abs(r-k)
    mx=max(h,mx)    
    if s[i-1]<s[i]>s[i+1]:
        if g==1:
            g=0
        elif g==0:
            g=1
print(mx)
