for i in range(0,100):
    b=bin(i)[2:]
    if i%2==0:
        b+='01'
    else:
        b+='10'
    R=int(b,2)
    if R>130:
        print(R)
