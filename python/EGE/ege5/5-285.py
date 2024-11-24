for N in range(1,1000):
    b=bin(N)[2:]
    if N%2==0:
        b=b+'10'
    else:
        b='1'+b+'01'
    R=int(b,2)
    if R>516:
        print(N)
