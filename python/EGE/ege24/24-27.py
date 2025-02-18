#s='xxCFEFCEFCEFCEddddxxxxxDddddCFEFCECFECFECFECFE'
s=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24_27.txt').read()
i=0
k=0
kmax=0
while i<len(s)-2:
    if s[i]+s[i+1]+s[i+2] in ['CFE','FCE']:
        k+=1
        i+=3
        kmax=max(kmax,k)
    else:
        k=0
        i+=1
print(kmax)
