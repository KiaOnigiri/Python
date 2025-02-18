f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24var08.txt')
k=21
s=f.read()
#s='ccccABcccccccABccccABccccccccccABABABcccccc'
s=s.split('AB')
s=[len(x) for x in s]
mx=(0,-1)
for i in range(len(s)-k):
    mx=max(mx,(sum(s[i:i+k+1])+2+k*2,i))
print(mx,len(s))
