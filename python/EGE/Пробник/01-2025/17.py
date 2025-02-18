f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Пробник/01-2025/files/17_19249.txt')
s=f.read().splitlines()
s=[int(x) for x in s]
mxs=max([x for x in s if len(str(abs(x)))==5 and str(x)[-2:]=='43'])
b=[]
for i in range(len(s)-2):
    troyka=[s[i],s[i+1],s[i+2]]
    ans1=[1 for x in troyka if len(str(abs(x)))==5 and str(x)[-2:]=='43']
    sumsquare=sum([x**2 for x in troyka])
    if sum(ans1)>=1 and sumsquare<=(mxs**2):
        b.append(sumsquare)
print(len(b),min(b))
