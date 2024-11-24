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
for i in range(2807,8558+1):
    if inAny(i,2)[-2:]==[1,1] and inAny(i,9)[-1]==5:
        c.append(i)
print(max(c),sum(c))
