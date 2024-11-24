def chered(x):
    g='ЛГРФМ'
    s='ОАИ'
    if x[0] in s:
        flag='S'
    if x[0] in g:
        flag='G'
    for i in range(1,len(x)):
        if x[i] in g and flag=='S':
            flag='G'
            continue
        elif x[i] in s and flag=='G':
            flag='S'
            continue
        else:
            return False
    return True


a='01234567'
k=0
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    x=x1+x2+x3+x4+x5
                    if x1!='0' and x.count('6')==1 and '16' not in x and '61' not in x and '36' not in x and '63' not in x and '56' not in x and '65' not in x and '76' not in x and '67' not in x:
                        k+=1
print(k)
