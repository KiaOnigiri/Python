from itertools import *
k=1
for x in product('AOY', repeat=5):
    x=''.join(x)
    if k==170:
        print(x)
    k+=1
#YAAYO
