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


for i in range(1,3000):
    if inAny(4**2015+2**i-2**2015+15,2).count(1)==500:
        print(i)
#2510
