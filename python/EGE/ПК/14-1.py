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


print(inAny(3**2017+9**1000-27,3).count(2))
#1997
