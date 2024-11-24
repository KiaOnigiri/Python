def inAny(x,y):
    ost=''
    while x>0:
        ost+=str(x%y)
        x=x//y
    ost=ost[::-1]
    return ost


for N in range(1,2000):
    b=inAny(N,3)
    if sum([int(x) for x in b])%3==0:
        b='20'+b
    else:
        b='10'+b
    R=int(b,3)
    if R<100:
        print(N)
