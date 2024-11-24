for i in range(1,99+1):
    b=bin(i)[2:]
    b+=b[-1]
    b+=str(b.count('1')%2)
    b+=str(b.count('1')%2)
    R=int(b,2)
    if R>97:
        print(i,R)
