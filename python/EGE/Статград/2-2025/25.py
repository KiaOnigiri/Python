from itertools import product
def prime(x):
    if x%1!=0: return False
    for y in range(2,int(x**0.5)+1):
        if x%y==0: return False
    return True
for i in range(5):
    for c in product('0123456789',repeat=4):
        c=''.join(c)
        c1=c[:i]
        c2=c[i:]
        x=int(f'1{c1}42{c2}81')
        if prime(x**0.5):
            print(x)
