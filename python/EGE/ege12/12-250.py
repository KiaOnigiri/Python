for n in range(185,200):
    s='1'*n
    while '1111' in s:
        s=s.replace('1111','2',1)
        s=s.replace('22','11',1)
    print(n,s)
