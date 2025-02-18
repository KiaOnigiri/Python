s=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24var09-12.txt').read()
s=s.replace('12','A')
s=s.replace('21','A')
s=s.replace('13','A')
s=s.replace('31','A')
s=s.split('A')
print(len(s[0])+1,len(max(s, key=len))+2,len(s[-1])+1)
#339
