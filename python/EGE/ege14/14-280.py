def inAny(x,y):
    m=[]
    while x>0:
        f=x%y
        if f>=10:
            f=chr(ord('A')-10+f)
        m.append(f)
        x//=y
    m.reverse()
    return m


k=0
for i in range(2,11):
    print(i,list(reversed(sorted(inAny(430,i)))),inAny(430,i))
    if list(reversed(sorted(inAny(430,i))))==inAny(430,i):
        k+=i
print(k)
#15
