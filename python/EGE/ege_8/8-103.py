'''
def chered(x):
    g='ОАЕ'
    s='КМТ'
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
'''




a='КУПЧИХА'
k=0
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    for x6 in a:
                        for x7 in a:
                            x=x1+x2+x3+x4+x5+x6+x7
                            if len(x)==len(set(x)) and x1!='Ч' and 'ИАУ' not in x:
                                k+=1
                                print(x)
print(k)
