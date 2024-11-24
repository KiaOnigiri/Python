def Add(c):
    k=0
    k1=0
    for x in c:
        if x%2==0:
            k+=1
        else:
            k1+=1
    return [k,k1]

#from random import *
#n=10
#a=[choice((2,1,0,3,4,20,40,0)) for _ in range(n)]
f=open('D:/python/EGE/ege27/27-data/35/27-35b.txt')
a=f.read().splitlines()
a=a[1:]
a=[int(x) for x in a]
#print(a)

c=[]
b=[]
for x in a:
    if x!=0:
        c.append(x)
    else:
        b.append(Add(c))
        
        c=[]
if c:
    b.append(Add(c))
print(b)
k2=0
for i in range(len(b)):
    k=0
    k1=0
    for j in range(i+1,len(b)):
        k+=b[j][0]
        k1+=b[j][1]
    k*=b[i][0]
    k1*=b[i][1]
    k2+=k1+k
print(k2)
