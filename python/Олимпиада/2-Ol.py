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



m=[]
A,B=map(int, input().split())
for i in range(A,B+1):
    m.append('X')
    m.append(''.join(map(str, inAny(i,2))))
m.remove('X')
x=1
while True:
    mm=m.copy()
    for i in range(len(m)):
        if m[i]=='X':
            if x>9:
                mm[i]=chr(ord('A')+x-10)
            else:
                mm[i]=x
    m1=''.join(map(str, mm))
    if (int(m1,x+2))%(x+1)==0:
        break
    x+=1
print(x)
