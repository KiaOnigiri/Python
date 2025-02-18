s=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24-31.txt').read()
for x in 'GHIJKLMNOPQRSTUVWXYZ':
    s=s.replace(x,'!')
s=s.split('!')
print(len(max(s,key=len)))
