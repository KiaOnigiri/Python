def inAny(x,y):
    x=int(x)
    if x==0:
        return '0'
    b=[]
    while x>0:
        ost=x%y
        if ost>9:
            ost=chr(ord('A')+ost-10)
        b.append(ost)
        x//=y
    b.reverse()
    z=''
    for c in b:
        z+=str(c)
    return z
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
    return str(a)



#g=+int(fromAny(('4'+inAny(str(x),100)+inAny(str(y),100)+'60'),59))-int(fromAny(('24'+inAny(str(y),100)+'9'),27)))
#print(fromAny('ABC25',15),inAny('3599',16))
#print(inAny(str(0),100))
#print('35'+inAny(str(0),100))
b=[]
for y in range(6,27):
    for x in range(0,y):
        b.append(int(fromAny(('35'+inAny(str(x),100)),y))+int(fromAny(('4'+inAny(str(x),100)+inAny(str(y),100)+'60'),59))-int(fromAny(('24'+inAny(str(y),100)+'9'),27)))
print(len(set(b)))
