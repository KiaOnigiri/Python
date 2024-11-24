def mult(x):
    x=str(x)
    x=[int(z) for z in x]
    k=1
    for v in x:
        k*=v
    if k!=0:
        return k
    else:
        return 47346265
def inAny(x,y):
    d=[]
    while x>0:
        ost=x%y
        if ost>9:
            ost=chr(ord('A')+ost-10)
        d.append(ost)
        x//=y
    d.reverse()
    return int(''.join(map(str, d)))


b=[]
for i in range(12345,67890+1):
    c=inAny(i,8)
    c=str(c)
    c=[int(p) for p in c]
    if sum(c)==19 and mult(inAny(i,8))%5==0:
        b.append(i)
print(len(b),min(b))
