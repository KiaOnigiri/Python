for i in range(0,100+1):
    b=bin(i)[2:]
    b=b[::-1]
    r=int(b,2)
    if r==7:
        print(i)
