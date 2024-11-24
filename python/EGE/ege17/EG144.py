def dels(x):
    d=[1,x]
    y=2
    while y*y<x:
        if x%y==0:
            d.append(y)
            d.append(x//y)
        y+=1
    if y*y==x:
        d.append(y)
    return d


b=[]
for i in range(45000,46000+1):
    k1=len(set(dels(i))&{9,11,13,15})
    k2=len(set(dels(i))&{25,33,40,45})
    if k1<k2:
        b.append(i)
print(len(b),int(sum(b)/len(b)))
