f=open('17.txt')
s=f.read().splitlines()
s=[int(x) for x in s]
mx=max([x for x in s if str(x)[-3:] == '123'])
b=[]
for i in range(len(s)-2):
    t3k=[s[i],s[i+1],s[i+2]]
    k1=[1 for x in t3k if 10000<=abs(x)<100000]
    k2=[1 for x in t3k if x%3==0]
    k3=sum(t3k)>mx
    if sum(k1)>=2 and sum(k2)==1 and k3:
        b.append(sum(t3k))
print(len(b),max(b))
