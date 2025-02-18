f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24var09-12.txt')
s=f.read()
s=s.replace('12','B')
s=s.replace('21','B')
print(len(max(s.split('B'), key=len)))
s=s.split('B')
mx=0
for i in range(len(s)):
    if mx<len(s[i]):
        mx=len(s[i])
        imx=i
print(len(s),imx)
