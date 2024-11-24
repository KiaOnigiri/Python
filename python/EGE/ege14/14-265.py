def inAny(x,y):
    m=[]
    while x>1:
        f=x%y
        if f>=10:
            f=chr(ord('A')-10+f)
        m.append(f)
        x//=y
    return m


k=0
for i in range(2,11):
    if len(set(inAny(1755,i)))==len(inAny(1755,i)):
        k+=i
print(k)
#15
