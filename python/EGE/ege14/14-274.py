def inAny(x,y):
    m=[]
    while x>1:
        f=x%y
        if f>=10:
            f=chr(ord('A')-10+f)
        m.append(f)
        x//=y
    return m


print(inAny(26**2+169-11,13).count('C'),inAny(26**2+169-11,13).count(2))
#2
