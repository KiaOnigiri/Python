def inAny(x,y):
    m=[]
    while x>0:
        f=x%y
        if f>=10:
            f=chr(ord('A')-10+f)
        m.append(f)
        x//=y
    return m


a=''
for x in range(23):
    f=str(x)
    if x>=10:
        f=chr(ord('A')-10+x)
    a+=f
print(a)
for x in a:
    if (int(f'1{x}1{x}1{x}1{x}1',23)+int(f'20{x}24',23)+int(f'1{x}235',23))%22==0:
        print((int(f'1{x}1{x}1{x}1{x}1',23)+int(f'20{x}24',23)+int(f'1{x}235',23))//22,x)
