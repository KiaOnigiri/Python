from itertools import *
c='НРМТК'
b=[]
for x in c:
    b.append(f'Ф{x}')
    b.append(f'{x}Ф')
#print(list(sorted(set(b))))
cnt=0
for x in list(set(permutations('ИНФОРМАТИКА'))):
    if all([smth not in ''.join(x) for smth in b]):
        cnt+=1
print(cnt)
#2721600
