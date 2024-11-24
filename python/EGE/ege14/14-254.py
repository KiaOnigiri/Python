def inAny(x,y):
    m=[]
    while x>1:
        m.append(x%y)
        x//=y
    return m


s=43*7**103-21*7**57+98
print(sum(inAny(s,7)))
#276
