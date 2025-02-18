s=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24-21.txt').read()
i=0
k=0
mx=0
while i<len(s)-2:
    if s[i].isdigit() and  s[i+1].isdigit() and s[i+2].isalpha():
        k+=1
        i+=3
        mx=max(mx,k)
    else:
        k=0
        i+=1
print(mx)
