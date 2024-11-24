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


x=1
b=[]
k=0
while x!=0:
    x=int(input())
    b.append(x)
b.remove(0)
m=[]
h=0
for i in range(len(b)):
    b2=inAny(b[i],2)
    print(b2)
    if len(b2)%3!=0:
        b2.reverse()
        b2.append(0)
        b2.reverse()
    if len(b2)%3!=0:
        b2.append(0)
    print(b2)
    for j in range(2,len(b2)+1,3):
        print(j,b2[j])
        if b2[j-2]+b2[j-1]==2 or b2[j-2]+b2[j-1]==0 and b2[j]==0:
            print('!')
            continue
        elif b2[j-2]+b2[j-1]==1 and b2[j]==1:
            print('!')
            continue
        k+=1
    if k==0:
        m.append(int(''.join(map(str, b2)),2))
    else:
        h+=1
        k=0
    print(m)
print(max(m),h)
            

