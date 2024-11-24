from itertools import *
k=1
for x in product('AOY', repeat=5):
    x=''.join(x)
    print(x,k)
    if k==125:
        print(x)
    k+=1
#OOOYO
