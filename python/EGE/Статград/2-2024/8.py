from itertools import *
k=1
cnt=0
for x in product('АЕКНРС',repeat=10):
    x=''.join(x)
    #print(k,x)
    k+=1
    if k%3==0 and x[0] in 'КНРС' and x.count('Р')==1:
        cnt+=1
print(cnt)
