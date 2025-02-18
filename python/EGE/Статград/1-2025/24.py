f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Статград/1-2025/Доп/24.txt')
s=f.read()
f.close()
s=s.replace('B',' ')
s=s.replace('C',' ')
s=s.replace('D',' ')
s=s.replace('--',' ')
s=s.replace('-*',' ')
s=s.replace('**',' ')
s=s.replace('*-',' ')
s=s.replace('A*',' ')
s=s.replace('A-',' ')
s=s.replace('6A',' A')
s=s.replace('5A',' A')
s=s.replace('4A',' A')
s=s.replace('3A',' A')
s=s.replace('2A',' A')
s=s.replace('1A',' A')
s=s.replace('2A',' A')
s=s.replace('*A',' A')
s=s.replace('-A',' A')
s=s.split()
kmax=-1
klen=''
for x in s:
    if 'A' in x and x[-1] not in ['-','*']:
        if len(x)>kmax:
            kmax=len(x)
            klen=x
print(kmax,klen)
