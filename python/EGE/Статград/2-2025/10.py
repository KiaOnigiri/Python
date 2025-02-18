from fnmatch import *
f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Статград/2-2025/Доп/10/Понедельник начинается в субботу.txt')
s=f.read().split()
f.close()
k=0
for x in s:
    if fnmatch(x,'от*') and len(x)==4:
        k+=1
        print(x)
print(k)
#193+2
#2422
