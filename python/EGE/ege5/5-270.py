a=[]
for N in range(1,200):
    b=bin(N)[2:]
    if N%2==1:
        b='10'+b+'11'
    else:
        b='1'+b+'00'
    R=int(b,2)
    if R>1023:
        a.append(R)
print(sorted(a))
