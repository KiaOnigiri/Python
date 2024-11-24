for N in range(1,1000):
    b=bin(N)[2:]
    if N%2==0:
        b='10'+b[2:]+'0'
    else:
        b='11'+b[2:]+'1'
    R=int(b,2)
    if R>=16:
        print(N)
