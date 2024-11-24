def inAny(x,y):
    b=[]
    while x>0:
        ost=x%y
        if ost>9:
            ost=chr(ord('A')+ost-10)
        b.append(ost)
        x//=y
    b.reverse()
    return b
c=[]
for i in range(1000,9999+1):
    if len(inAny(i,6))<=5 and (inAny(i,6)[-2:]==[1,3] or inAny(i,6)[-2:]==[1,4]):
        c.append(i)
print(len(c),max(c))
