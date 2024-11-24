for N in range(1,100):
    b=bin(N)[2:]
    if N%2==1:
        b='1'+b+'11'
    else:
        b='11'+b+'00'
    R=int(b,2)
    if R<127:
        print(N,R)
