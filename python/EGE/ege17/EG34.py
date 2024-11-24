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


r=[]
for i in range(1000,9999):
    if i%5!=0 and i%7!=0 and i%11!=0 and len(inAny(i,4))==6:
        r.append(i)
print(max(r),min(r))
