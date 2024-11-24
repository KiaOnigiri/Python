for N in range(100,1000):
    b=[int(i) for i in str(N)]
    b.sort()
    mx=int(str(b[2])+str(b[1]))
    if b.count(0)==0:
        mn=int(str(b[0])+str(b[1]))
    elif b.count(0)==1:
        mn=int(str(b[1])+str(b[0]))
    else:
        mn=mx
    if mx-mn==63:
        print(N)
