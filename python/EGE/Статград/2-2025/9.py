from time import *
f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Статград/2-2025/Доп/09.txt')
t1=time()
s=f.read().splitlines()
s=[[int(y) for y in x.split()]for x in s]
s0=[x[0] for x in s]
s1=[x[1] for x in s]
s2=[x[2] for x in s]
s3=[x[3] for x in s]
s4=[x[4] for x in s]
s5=[x[5] for x in s]
print(len(s))
k=0
for x in s:
    interest=0
    sr=sum(x)/len(x)
    for i in range(len(x)):
        if x.count(x[i])==1 and eval(f's{i}').count(x[i])>=331\
           and x[i]>sr:
            interest+=1
    if interest==1:
        print(x)
        k+=1
        if k==10:
            break
print(k)
#4175
t2=time()
print(t2-t1)
