s=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24_24.txt').read()

k=1
mx=0
for i in range(len(s)-1):
    if s[i]+s[i+1] in ['FE','EF']:
        k+=1
        mx=max(mx,k)
    else:
        k=1
print(mx)
