from itertools import *
k=1
for x in product('AKPY', repeat=5):
    x=''.join(x)
    if k==150:
        print(x)
    k+=1
#APKKK
