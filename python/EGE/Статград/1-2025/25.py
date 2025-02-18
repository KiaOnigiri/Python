def M(x):
    b=[]
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            b.append(x//i)
            if len(b)==2:
                return b[0]+b[1]
    if len(b)==1 and b[0]!=x**0.5:
        return b[0]+x//b[0]
    else:
        return 0
    '''
    if len(b)<2:
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                b.append(i)
                if len(b)==2:
                    break
    b=list(set(b))
    if len(b)<2:
        return 0
    else:
        return sum(sorted(b)[-2:])
    '''
for N in range(110250000,110300000+1):
    if str(M(N))[-4:]=='1002':
        print(N)
