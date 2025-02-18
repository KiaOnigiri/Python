s=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24_23.txt').read()
sogl='CDF'
glas='AOa'
mx=0
k=0
for i in range(len(s)-3):
    if s[i] in sogl and s[i+1] in glas and s[i+2] in glas and s[i+3] in sogl:
        mx=max(mx,k+3)
        k=0
    else:
        k+=1
        mx=max(mx,k)
mx=max(mx,k+3)
print(mx)
