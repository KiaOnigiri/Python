def dels(x):
    b=[1,x]
    for y in range(2,int(x**0.5)+1):
        if x%y==0:
            b.append(y)
            b.append(x//y)
    return sorted(set(b))


c=[]
for i in range(12356,76435+1):
    if len(dels(i))>15:
        c.append(i)
print(len(c),max(c))
