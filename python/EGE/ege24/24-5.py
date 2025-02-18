f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24var05.txt')
s=f.read()
k=3
s=s.split('A')
s=[len(x) for x in s]
mx=0
for i in range(len(s)-k):
    mx=max(mx,sum(s[i:i+k+1])+k)
print(mx)
#501
