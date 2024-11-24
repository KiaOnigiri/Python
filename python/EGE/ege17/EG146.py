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
    d=[z for z in d if len(str(z))==2]
    return d


b=[]
for i in range(25552,58885+1):
    if len(dels(i))>=15:
        b.append(i)
print(max(b),len(b))
