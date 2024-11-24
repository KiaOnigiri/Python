for N in range(1,100):
    b=bin(N)[2:]
    b+=str(b.count('1')%2)
    b+=str(b.count('1')%2)
    R=int(b,2)
    if R>130:
        print(f'N={N}, R={R}')
    
