def inAny(x,y):
    ost=''
    while x>0:
        ost+=str(x%y)
        x=x//y
    ost=ost[::-1]
    return ost


for N in range(1,2000):
    b=inAny(N,4)
    b=str(N%2)+b+str(N%3)
    b=int(b,4)
    if 10<=b<100:
        print(b,N)
