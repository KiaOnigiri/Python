def chered(x):
    g='АИ'
    s='БТС'
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


a='АББАТИСА'
b=[]
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    for x6 in a:
                        for x7 in a:
                            for x8 in a:
                                x=x1+x2+x3+x4+x5+x6+x7+x8
                                if chered(x) and x.count('Б')==2 and x.count('А')==3 and x.count('С')==1 and x.count('И')==1 and x.count('Т')==1:    
                                    b.append(x)
print(len(set(b)))
