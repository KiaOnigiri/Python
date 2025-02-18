f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Статград/2-2025/Доп/26.txt')
s=f.read().splitlines()
s=s[1:]
s=[[int(y) for y in x.split()] for x in s]
s1=[]
for x in s:
    if sum([smth for smth in x[1:]])<=0:
        continue
    s1.append([x[0],sum([smth for smth in x[1:]]),sum([smth for smth in x[1:] if smth>0]),len([smth for smth in x[1:] if smth!=0])])
s1.sort(key=lambda x: [x[1],x[2],x[3],-x[0]], reverse=True)
print(len(s1))
#2381+2
#print(s1[2380:2380+20])
ans1=s1[2383]
s1=s1[2383:]
print(len(s1)*0.1)
#476+2
print(s1[475:475+20])
print(ans1)
#35669,478
