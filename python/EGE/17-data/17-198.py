def inAny(x,y):
    b=[]
    while x>0:
        b.append(x%y)
        x//=y
    b.reverse()
    return b


f=open("17-10.txt")
c=f.read().splitlines()
c=[int(z) for z in c]
b=[]
for i in range(1,len(c)):
    s7=inAny(c[i-1]+c[i],7)
    if s7==s7[::-1]:
        b.append(int(''.join([str(z) for z in s7]),7))
print(len(b),inAny(max(b),7))
