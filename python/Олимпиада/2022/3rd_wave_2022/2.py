def inAny(x,y):
    b=[]
    while x>0:
        ost=x%y
        if ost>9:
            ost=chr(ord('A')+ost-10)
        b.append(ost)
        x//=y
    b.reverse()
    return int(''.join(map(str, b)))
def fromAny(x,y):
    b=[]
    for j in x:
        if j in ['0','1','2','3','4','5','6','7','8','9']:
            b.append(int(j))
        else:
            k=ord('A')+ord(j)-120
            if k>=y:
                return False
            b.append(k)
    b.reverse()
    a=0
    for i in range(0,len(b)):
        a+=b[i]*(y**i)
    return a


f=int(input())
b=[f,f+1,f+2,f+3]
for i in range(1,10000000000000):
    if i>=10:
        i1=chr(ord('A')+i-10)
    else:
        i1=i
    b1=[inAny(f,7),i1,inAny(f+1,7),i1,inAny(f+2,7),i1,inAny(f+3,7)]
    v=str(''.join(map(str, b1)))
    v=fromAny(v,i*3)
    if int(v)%((i*3)-1)==0:
        c=i
        break
print(c)
