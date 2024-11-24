'''
f=open('27-A.txt')
s=f.read().splitlines()
s=[int(x) for x in s]
k=s[0]
n=s[1]
s=s[2:]
smx=0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        for l in range(j+1,len(s)):
            if l-i>=3*k:
                smx=max(smx,s[i]+s[j]+s[l])
                p1=s[i]
                p2=s[l]
                ps=s[j]
    
print(f'{p1}+{ps}+{p2}={smx}')
'''
'''
f=open('27-B.txt')
s=f.read().splitlines()
s=[int(x) for x in s]
k=s[0]*3
n=s[1]
s=s[2:]
print(max(s))
mx2=min(s)-1
imx2=0
smx=mx2*2
for i in range(k,n):
    if s[i-k]>mx2:
        mx2=s[i-k]
        imx2=i-k
    ps=max(s[imx2+1:i])
    if mx2+s[i]+ps>smx:
        smx=mx2+s[i]+ps
        p1=mx2
        p2=s[i]
        p3=ps
    
print(f'{p1}+{p3}+{p2}={smx}')'''
f=open('27-B.txt')
a=f.read().splitlines()
a=[int(x) for x in a]
k=a[0]
n=a[1]
a=a[2:]
m2,m1=sorted(a[:3*k])[-2:]
mx3k=-1000000000000000
smx=-1000000000000000000000
for i in range(3*k,n):
    mx3k=max(mx3k,a[i-3*k])
    if m1==mx3k:
        smx=max(smx,mx3k+m2+a[i])
    else:
        smx=max(smx,mx3k+m1+a[i])
    #print(a[i],m1,m2)
    m2,m1=sorted([a[i],m2,m1])[-2:]
print(smx)
    
