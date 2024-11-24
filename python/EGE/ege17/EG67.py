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


b=[]
for i in range(100001,900009+1):
    k=inAny(i,7)
    k=int(''.join(map(str, k)))
    k=k%10
    g=i%10
    if k+g==10 and i%11==0 and i%55!=0:
        b.append(i)
print(max(b),len(b))
