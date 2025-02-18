s=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24var09-12.txt').read()
s=s.split('000')
print(len(s[0])+2,len(max(s, key=len))+4,len(s[-1])+2)
#7684
