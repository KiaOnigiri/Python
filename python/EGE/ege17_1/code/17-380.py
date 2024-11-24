f=open('../17-380.txt')
s=f.read().splitlines()
s=[int(z) for z in s]
smx=max([x for x in s if str(x)[-2:]=='25'])
b=[]
for i in range(len(s)-2):
    troyka=[s[i],s[i+1],s[i+2]]
    k=sum([1 for x in troyka if len(str(abs(x)))==4])
    if k<=2 and sum(troyka)<=smx:
        b.append(sum(troyka))
print(len(b),max(b))
