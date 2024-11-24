def chered(x):
    g='13579'
    s='02468'
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


a='0123456789'
k=0
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
                                if x1=='0':
                                    continue
                                
                                if int(x)%5==0 and chered(x) and len(x)==len(set(x)):
                                    k+=1

print(k)
