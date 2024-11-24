for n in range(101,1000):
    s='5'*n
    while '555' in s or '888' in s:
        s=s.replace('555','8',1)
        s=s.replace('888','55',1)
    if '8' not in s:
        print(n)
        break
