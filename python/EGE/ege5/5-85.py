for N in range(1,50):
    b=bin(N)[2:]
    if b.count('1')%2==0:
        b+='1'
    else:
        b+='0'
    if b.count('1')%2==0:
        b+='1'
    else:
        b+='0'
    R=int(b,2)
    if R>54:
        print(f'N={N}, R={R}')
