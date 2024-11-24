for N in range(1,100):
    
    b=bin(N)[2:]
    if b.count('1')%2==0:
        b=b+'0'
    else:
        b+='1'

    if b.count('1')%2==0:
        b=b+'0'
    else:
        b+='1'

    R=int(b,2)
    if R>130:
        
        print('N={} R={}'.format(N,R))
