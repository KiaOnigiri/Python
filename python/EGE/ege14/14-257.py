def inAny(x,y):
    m=[]
    while x>1:
        m.append(x%y)
        x//=y
    return m


k=0
for i in range(2,11):
    if 1 not in inAny(3456,i) and 3 not in inAny(3456,i) and 5 not in inAny(3456,i) and 7 not in inAny(3456,i) and 9 not in inAny(3456,i):
        k+=i
print(k)
#23
