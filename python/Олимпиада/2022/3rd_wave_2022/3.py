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


k=input()
knorm=inAny(int(k,16),2)
while len(knorm)%4!=0:
    knorm.reverse()
    knorm.append(0)
    knorm.reverse()
print(knorm)
b1=[]
b2=[]
for i in range(3,len(knorm),4):
    if (knorm[i-3]+knorm[i-2]+knorm[i-1])%2==knorm[i]:
        b1.append('1')
    else:
        b1.append('0')
    b2.append(knorm[i-3])
    b2.append(knorm[i-2])
    b2.append(knorm[i-1])
b2=''.join(map(str, b2))
if '0' in b1:
    print(-1)
else:
    print(int(b2,2))
