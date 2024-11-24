def inAny(x,y):
    m=''
    while x>1:
        m+=str(x%y)
        x//=y
    return m


for i in range(4,10+1):
    if int('12',i)*int('13',i)==int('211',i):
        print(i)
#5
