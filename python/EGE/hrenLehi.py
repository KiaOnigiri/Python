for n in range(100):
    s = '7' + '1'*(n+1) + '2'*(n+2) + '3'*(n+3)

    while '71' in s or '72' in s or '73' in s:
        if '71' in s:
            s = s.replace('71','227', 1)
        if '72' in s:
            s = s.replace('72','37', 1)
        if '73' in s:
            s = s.replace('73','17', 1)
    
    print('!')
    res = sum([int(x) for x in s]) 

    if res == 9*n:
        print(n)
        break
