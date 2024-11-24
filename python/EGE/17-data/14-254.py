def inAny(x,y):
    b=[]
    while x>0:
        b.append(x%y)
        x=x//y
    b.reverse()
    return b



x=43*7**103-21*7**57+98
x1=inAny(x,7)
print(sum(x1))
