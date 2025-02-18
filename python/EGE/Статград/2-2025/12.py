from itertools import *
'''
b=[]
for ones in range(0,100):
    for twos in range(0,100):
        s='2'*ones+'1'*twos
        while '111' in s or '22' in s:
            s=s.replace('111','2',1)
            s=s.replace('222','1',1)
            s=s.replace('221','1',1)
            s=s.replace('122','1',1)
            s=s.replace('22','2',1)
        if s.count('2')==9:
            b.append(s.count('2'))
print(sorted(list(set(b))))'''
'''
s='211'*8+'111'
while '111' in s or '22' in s:
    s=s.replace('111','2',1)
    s=s.replace('222','1',1)
    s=s.replace('221','1',1)
    s=s.replace('122','1',1)
    s=s.replace('22','2',1)
print(s.count('1'),s.count('2'),s)'''
#12
#21
#211
#121 2 2 2
#112
k=set()
for x in product('12',repeat=28):
    s=''.join(x)
    while '111' in s or '22' in s:
        s=s.replace('111','2',1)
        s=s.replace('222','1',1)
        s=s.replace('221','1',1)
        s=s.replace('122','1',1)
        s=s.replace('22','2',1)
    if s.count('2')==9:
        k.add(s)
        #print(f'begin={''.join(x)},end={s}')
print(len(k))
#111111111222212121212121212
