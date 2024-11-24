from itertools import product
k=0
for x in product('0123456789AB',repeat=5):
    x=''.join(x)
    if x[0]!='0' and x.count('7')==1 and x.count('9')+x.count('A')+x.count('B')<=3:
        k+=1
print(k)
