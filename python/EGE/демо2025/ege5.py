for N in range(1,13):
    r=bin(N)[2:]
    if r[-1]=='0':
        r='10'+r
    else:
        r='1'+r+'01'
    R=int(r,2)
    print(N,R)
