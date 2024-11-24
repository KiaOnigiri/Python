f=open('17.txt')
s=f.read().splitlines()
s=[int(x) for x in s]
mx=max([x for x in s if str(x)[-2:]=='19'])
b=[]
for i in range(2,len(s)):
    k=[s[i],s[i-1],s[i-2]]
    if len([j for j in k if 1000<=j<=9999])==2:
        if any([j%3==0 for j in k]):
            if sum(k)>mx:
                b.append(sum(k))
print(len(b),max(b))
            
