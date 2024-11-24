def inAny(x,y):
    ost=''
    while x>0:
        ost+=str(x%y)
        x=x//y
    ost=ost[::-1]
    return ost


for N in range(1,100):
    b=inAny(N,6)
    b+=b[-1]
    b=int(b,6)
    b=bin(b)[2:]
    b+=b[-1]
    R=int(b,2)
    if R<344:
        print(N,R)
