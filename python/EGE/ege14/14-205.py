def inAny(x,y):
    m=''
    while x>1:
        m+=str(x%y)
        x//=y
    return m


s=64**30+2**300-32
print(inAny(s,4).count('3'))
#87
