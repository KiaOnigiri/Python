from time import time
t1=time()
f=open('26-75.txt')
s=f.read().splitlines()
NOfPas=int(s[0])
s=s[1:]
s=[[int(q) for q in z.split()] for z in s]
s.sort()
mn=min([z[0] for z in s])
mx=max([z[1] for z in s])
k=0
mxk=0
t=0
for i in range(mn,mx+1):
    flag=True
    for j in s:
        if j[0]<=i<=j[1]:
            k+=1
            mxk=max(mxk,k)
            if flag:
                t+=1
                flag=False
    k=0
print(mxk,t)
t2=time()
print(t2-t1)
