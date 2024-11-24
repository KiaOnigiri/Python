def inAny(x,y):
    b=[]
    while x>0:
        ost=x%y
        if ost>9:
            ost=chr(ord('A')+ost-10)
        b.append(ost)
        x//=y
    b.reverse()
    return ''.join(map(str, b))

x=int(input('Какое число переводится: '))
y=int(input('В какую систему переводится: '))
print(inAny(x,y))
