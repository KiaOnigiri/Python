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
for i in range(20000,30000+1):
    if len(set(dels(i))&{7,11,13,19})==2:
        b.append(i)
print(len(b),int(sum(b)/len(b)))
