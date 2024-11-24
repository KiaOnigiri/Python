def inAny(x,n):
    b=[]
    while x>0:
        b.append(str(x%n))
        x//=n
    b.reverse()
    return ''.join(b)

mxl=[]
for n in range(1,2000):
    r=inAny(n,4)
    if n%4==0:
        r=r+r[-2:]
    else:
        r=r+inAny((n%4)*2,4)
    r=int(r,4)
    if r<261:
        mxl.append(n)
print(max(mxl))
'''n=12
r=inAny(n,4)
if n%4==0:
    r=r+r[-2:]
else:
    r=r+inAny((n%4)*2,4)
print(r)
r=int(r,4)
print(r)'''
