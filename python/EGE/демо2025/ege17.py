f=open('C:/python/EGE/демо2025/demo_2025_17.txt')
s=f.read().splitlines()
s=[int(x) for x in s]
mn=min(s)
b=[]
for i in range(1,len(s)):
    if s[i-1]%16==mn or s[i]%16==mn:
        b.append(s[i-1]+s[i])
print(len(b),max(b))
#1214 176024
