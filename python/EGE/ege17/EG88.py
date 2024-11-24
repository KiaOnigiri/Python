import time
def dels(x):
    b=[1,x]
    for j in range(2,int(x**0.5)+1):
        if x%j==0:
            if j==x//j:
                b.append(j)
            else:
                b.append(j)
                b.append(x//j)
    return b


t1=time.time()
kgr=[]
for i in range(54123,75321+1):
    d=dels(i)
    k=0
    for j in d:
        if 10<=j<=20:
            k+=1
    if k==5:
        kgr.append(i)
print(len(kgr),max(kgr))
t2=time.time()
print(t2-t1)
