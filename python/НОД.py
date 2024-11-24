def nod(x,y):
    while x!=y:
        if x>y:
            x=x-y
        if x<y:
            y=y-x
    return x


def dels(x):
    a=[]
    for i in range(1,x+1):
        if x%i==0:
            a.append(i)
    return a


x,y=12,36
print(dels(x))
print(dels(y))
print(set(dels(x))&set(dels(y)))
