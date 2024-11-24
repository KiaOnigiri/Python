from itertools import product
n=1
for x in product('бдекнтцчэ', repeat=6):
    x=''.join(x)
    if n%2==0 and 'н' not in x[0]+x[-1] and x.count('е')>=3:
        print(n,x)
        break
    n+=1   
#912
