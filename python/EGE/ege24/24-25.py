s=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24_25.txt').read()
i=0
k=''
kmax=''
while i<len(s)-2:
    if s[i] in 'BC' and s[i+1] in 'BC' and s[i+2]=='A':
        k+=s[i]+s[i+1]+s[i+2]
        kmax=max(kmax, k, key=len)
        i+=3
    else:
        k=''
        i+=1
print(kmax,len(kmax))
