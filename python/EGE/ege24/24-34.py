from itertools import *
s=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24-34.txt').read()
b=[]
for x in product('WVXYZ',repeat=3):
    b.append(''.join(x))
k=2
kmax=0
for i in range(len(s)-2):
    if s[i]+s[i+1]+s[i+2] in b:
        k=2
    else:
        k+=1
        kmax=max(k,kmax)
print(kmax)
#print(max(s, key=len),len(max(s, key=len)))
