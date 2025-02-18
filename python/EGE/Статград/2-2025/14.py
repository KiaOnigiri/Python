def inSeven(x):
    b=[]
    while x>0:
        b.append(x%7)
        x//=7
    return list(reversed(b))
b=inSeven(4*7**24+6*7**13+5*49**4+2*343**2+10-29059314)
print(b,b.count(6),b.count(0))
print(int('502000000',7))
'''
for x in range(1,100000):
    f=inSeven(4*7**24+6*7**13+5*49**4+2*343**2+10-x)
    if f.count(6)>f.count(0):
        print(x)
        break'''
#29059314
