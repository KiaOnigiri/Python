f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Статград/1-2025/Доп/17.txt')
s=f.read().splitlines()
f.close()
s=[int(x) for x in s]
mn=min(s)
mx=max(s)
mn3=mn%3
mx7=mx%7
b=[]
for i in range(1,len(s)):
    if (s[i-1]%3==mn3 or s[i]%3==mn3) and (s[i-1]%7==mx7 or s[i]%7==mx7):
        b.append(s[i-1]+s[i])
print(len(b),max(b))
#1415 199020
