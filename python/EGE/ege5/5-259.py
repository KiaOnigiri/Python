for N in range(2,100):
    b=bin(N)[2:]
    if b.count('0')==0:
        continue
    #adress=b.rfind('0')
    #b=b[:adress]+b[:2]+b[adress+1:]
    b=b[::-1]
    b=b.replace('0',b[-2:],1)
    R=int(b,2)
    if R==119:
        print(N)
