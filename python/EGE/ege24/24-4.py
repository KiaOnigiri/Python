def maxA(s,k):
    s=s.split('A')
    s=[len(x) for x in s]
    mx=0
    for i in range(len(s)-k):
        #curr='A'.join([str(y) for y in s[i:i+k+1]])
        #print(curr)
        mx=max(mx,sum(s[i:i+k+1])+k)
    return mx


f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24var04.txt')
s=f.read()
s=s.split('E')
mx=0
for x in s:
    mx=max(mx,maxA(x,700))
#s='ccAccccAAAccccAAcccccA'
print(mx)
