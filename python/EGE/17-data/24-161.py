f=open('24-s1.txt')
s=f.read().splitlines()
os=''.join(s)
mx=0
for i in range(len(s)):
    kA=s[i].count('Q')
    if kA>=mx:
        mx=kA
        imx=i
a=list(set(s[imx]))
mk=len(os)
imk=-1
for x in sorted(a):
    kX=s[imx].count(x)
    if kX<mk:
        mk=kX
        imk=x
print(imk,os.count(imk),sep='')
    
