for N in range(1,100):
    r=N-(N%8)+(N%2)
    r=bin(r)[2:]
    r+=str(sum([int(x) for x in r])%2)
    r+=str(sum([int(x) for x in r])%2)
    r=int(r,2)
    if r>97:
        print(r)
