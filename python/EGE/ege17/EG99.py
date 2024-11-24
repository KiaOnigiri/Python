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
k=[]
for i in range(100,1000000):
    if inAny(i,16)[0]=='B' and inAny(i,16)[-1]=='A' and i%12!=0:
        k.append(i)
print(len(k),max(k))
