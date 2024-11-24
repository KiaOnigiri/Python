f=open('24-s1.txt')
s=f.read().splitlines()
os=''.join(s)
mn=len(os)
for i in range(len(s)):
    kA=s[i].count('A')
    if kA<mn:
        mn=kA
        imx=i
a=list(set(s[imx]))
mk=0
imk=-1
for x in sorted(a):
    kX=s[imx].count(x)
    if kX>=mk:
        mk=kX
        imk=x
print(imk,os.count(imk),sep='')
    
