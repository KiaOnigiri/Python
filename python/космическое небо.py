f=open('f73e95c1739cab1b.txt','r', encoding="utf-8")
s=f.read().splitlines()
s1=[]
for x in s:
    d=x.split(' - ')
    s1.append(d)
f=input()
for x in s1:
    if x[0]==f:
        print(x[1])
