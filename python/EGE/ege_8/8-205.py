from itertools import *
import time


t1=time.time()
x=[z for z in permutations('МАРИНА') if z[0] not in 'АИ']
print(len(set(x)))
t2=time.time()
print(str(t2-t1)+' sec')
'''
t1=time.time()
q=[]
c='ТИКТОК'
for x1 in c:
    for x2 in c:
        for x3 in c:
            for x4 in c:
                for x5 in c:
                    for x6 in c:
                        s=x1+x2+x3+x4+x5+x6
                        if s.count('Т')==2 and s.count('К')==2 and s.count('О')==1 and s.count('И')==1:
                            q.append(s)
print(len(set(q)))
t2=time.time()
print(str(t2-t1)+' sec')
'''
