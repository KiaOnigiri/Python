f=open('C:/python/EGE/Пробник/24var01.txt')
s=f.read()
s='xxxAxxxxAxAxxxAxxAxxxxxAxxxx'
k=3
s=s.split('A')
s=[len(x) for x in s]
s=s[1:]
b=[]
for x in range(len(s)-k+1):
    b.append(sum(s[x:x+k-1])+k)
print(min(b))
