#print(len(max(open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24var09-12.txt').read().split('00'), key=len)))
f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24var09-12.txt')
s=f.read()
s=s.split('00')
mx=0
for i in range(len(s)):
    if len(s[i])>mx:
        mx=len(s[i])
        imx=i
print(len(s),imx)
