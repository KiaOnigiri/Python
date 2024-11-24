f=open('24-140.txt')
s=f.read()
k=-1
g=0
r=[]
n=-1
for i in range(len(s)):
    if s[i]=='D' and g==0:
        k=i
    if s[i]=='D' and g==1:
        n=i
    if s[i]=='D' and k!=-1 and n!=-1:
        r.append(abs(n-k)+1)
    if s[i]=='D':
        if g==0:
            g=1
        elif g==1:
            g=0
print(min(r))
