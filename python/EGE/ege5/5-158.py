for N in range(0,256):
    b=bin(N)[2:]
    b=(8-len(b))*'0'+b
    b=b.replace('1','2')
    b=b.replace('0','1')
    b=b.replace('2','0')
    R=int(b,2)
    result=R-N
    if result==99:
        print(N)

