def inThree(x):
    b=[]
    while x>0:
        b.append(str(x%3))
        x//=3
    return ''.join(list(reversed(b)))

d=[]
for n in range(3,300):
    r=inThree(n)
    if n%3==0:
        r+=r[-2:]
    else:
        r+=inThree(sum([int(x) for x in r]))
    r=int(r,3)
    if r>220:
        d.append(r)
print(min(d))
#222
