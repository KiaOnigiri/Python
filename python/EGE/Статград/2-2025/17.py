f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Статград/2-2025/Доп/17.txt')
s=[int(x) for x in f.read().splitlines()]
mx=max(s)%7
mn=min(s)%3
b=[]
for i in range(len(s)-2):
    trio=[s[i],s[i+1],s[i+2]]
    cnt1=sum([1 for x in trio if x%3==mn])
    cnt2=sum([1 for x in trio if x%7==mx])
    if cnt1==1 and cnt2>=2:
        b.append(sum(trio))
print(len(b),max(b))
