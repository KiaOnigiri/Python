from itertools import *
cnt=0
for x in product('01',repeat=20):
    if (5+x.count('1'))%3==0:
        cnt+=1
print(cnt)
