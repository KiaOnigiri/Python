f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24var02.txt')
s=f.read()
#s='ccccAccccAAccccAAAccAcAccccAAccccccccAAAAccc'
k=350
s=s.split('A')
s=[len(x) for x in s]
mx=0
for i in range(len(s)-k):
    #curr_str='A'.join(s[i:i+k+1])
    mx=max(mx,sum(s[i:i+k+1])+k)
print(mx)
    
