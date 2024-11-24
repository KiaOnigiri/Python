f=open('Faily_IN11_06022024_/17.txt')
s=f.read().splitlines()
s=[int(x) for x in s]
print(s[:5])
mx=max([x for x in s if str(x)[-3:]=='238'])
print(f'max={mx}')
b=[]
for i in range(2,len(s)):
    troy=[s[i-2],s[i-1],s[i]]
    k1=sum([1 for x in troy if len(str(x))==5])
    k2=sum([1 for x in troy if x%3==0])
    k3=sum([1 for x in troy if x%5==0])
    if 1<=k1<=2 and k2>k3 and sum(troy)>mx:
        b.append(sum(troy))
print(len(b),max(b))
