f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24var03.txt')
s=f.read()
#s='ccccAccccAAccccAAAccAcAccccAAccccccccAAAAccc'
k=500
s=s.split('A')
s=s[1:-1]
s=[len(x) for x in s]
mn=1000000000000
for i in range(len(s)-k+2):
    #print(s[i:i+k-1])
    mn=min(mn,sum(s[i:i+k-1])+k)
print(mn)   
#5678
