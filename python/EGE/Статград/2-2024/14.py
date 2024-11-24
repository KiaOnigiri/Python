def fromAny(x,n):
    x=x[::-1]
    sm=0
    for i,y in enumerate(x):
        if y.isalpha()==True:
            y=ord(y)-ord('A')+10
        sm+=int(y)*n**i
    return sm

#print(fromAny('1A',16))
for p in range(16,1000+1):
    c1=fromAny(f'AB267D1',p)
    c2=fromAny(f'F024A89',p)
    if (c1+c2)%(p-1)==0:
        print(p,c1,c2)
        break
