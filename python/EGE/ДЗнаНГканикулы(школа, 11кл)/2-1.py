from itertools import *

s='ПЯТЕРКА'
cnt=0
b=[''.join(smth) for smth in permutations('ЯЕА',2)]
#print(b)

for x1 in s:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                for x5 in s:
                    x=x1+x2+x3+x4+x5
                    if all([smth not in x for smth in b]):
                        cnt+=1
print(cnt)
#10663
