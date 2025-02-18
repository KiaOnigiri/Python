from itertools import *
cnt=0
for x in product('01',repeat=20):
    if x.count('1')%5!=0:
        cnt+=1
print(cnt)
