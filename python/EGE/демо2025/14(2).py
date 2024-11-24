def inAny(x,y):
    b=''
    while x>0:
        b+=str(x%y)
        x//=y
    return b[::-1]


for x in range(2030,1-1,-1):
    c=7**170+7**100-x
    c7=inAny(c,7)
    if c7.count('0')==71:
        print(x)
        break
