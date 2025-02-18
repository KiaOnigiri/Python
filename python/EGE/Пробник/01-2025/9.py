f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Пробник/01-2025/9.txt')
s=f.read().splitlines()
s=[[int(y) for y in x.split()] for x in s]
#print(s[:5])
k=1
ans=0
for x in s:
    usl=[y for y in x if x.count(y)==3]
    for y in x:
        if x.count(y)==1:
            nepovt=y
    if len(usl)==6 and (sum(usl)/len(usl))<nepovt:
        ans=k
    k+=1
print(ans)
print(s[17974])
        
        
