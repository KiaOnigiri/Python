f=open('17var01.txt')
s=f.read().splitlines()
s=[int(x) for x in s]
smin=min([x for x in s if str(x)[-2:]=='25'])
b=[]
for x in range(2,len(s)):
    troyka=[s[x-2],s[x-1],s[x]]
    ans1=sum([1 for y in troyka if len(str(y))==2])
    if ans1==1 and sum(troyka)<smin:
        b.append(sum(troyka))
print(len(b),max(b))
