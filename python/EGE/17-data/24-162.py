f=open('24-s1.txt')
s=f.read().splitlines()
os=''.join(s)
mn=len(os)
b=[]
for i in range(len(s)):
    for j in range(1,len(s[i])):
        if ord(str(s[i][j-1]))+1== ord(str(s[i][j])):
            b.append(1)
    kA=sum(b)
    if kA<mn and kA!=0:
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
    
