f=open('C:/python/EGE/Статград/1-2025/Доп/10/10.txt')
#s=f.read().split('–')
#s=' '.join(s).split()
s=f.read().split()
k=0
for word in s:
    if word[0].upper()=='А' and word[-1].upper()=='Я':
        k+=1
        print(word)
        
print(k-2)
