f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Статград/2-2025/Доп/24.txt')
s=f.read()
#s='AAAAAAAA6336939+259925'
for x in ['B','C','D','++','-','*']:
    s=s.replace(x,' ')
for x in 'A123456789+':
    s=s.replace(f'{x}A',f'{x} A')
s=s.replace('A+',' ')
s=s.split()
s=[x for x in s if x[0]=='A']
for i in range(len(s)):
    if s[i][-1]=='+':
        s[i]=s[i][:-1]
#s=[x[:-1] for x in s if x[-1]=='+']
for i in range(len(s)):
    if len(s[i])>1 and s[i][1]=='A':
        s[i]=s[i][1:]
s=[x[1:] for x in s]
s=[x for x in s if x!='']
s=[(sum([int(y) for y in x.split('+')]),x) for x in s]
s.sort(reverse=True)
