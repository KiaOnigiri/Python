def inAny(x,y):
    ost=''
    while x>0:
        ost+=str(x%y)
        x=x//y
    ost=ost[::-1]
    return ost
a=[]
for i in range(1,1000):
    b=inAny(i,4)
    if i%2!=0:
        b='2'+b+'11'
    else:
        b='13'+b+'02'
    r=int(b,4)
    if r>1000:
        a.append(r)
print(sorted(a))
