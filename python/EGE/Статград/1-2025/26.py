f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Статград/1-2025/Доп/26.txt')
s=f.read().splitlines()
s=s[1:]
s=[[int(y) for y in x.split()] for x in s]
s1=[]
for x in s:
    ss1=sum(x[1:])
    ss2=sum([t for t in x[1:] if t>0])
    ss3=10-x[1:].count(0)
    ss4=x[0]
    s1.append([ss1,ss2,ss3,ss4])

s1.sort(reverse=True,key=lambda x:(x[0],x[1],x[2],-x[3]))
#print(len(s1)//3)
k=0
print(s1[3195])
for x in s1:
    if s1[1499][:3]==x[:3]:
        k+=1
print(k)
#4229
#23
