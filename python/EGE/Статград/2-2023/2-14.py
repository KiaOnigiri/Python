def fromAny(x,y):
    x.reverse()
    sm=0
    for i in range(len(x)):
        sm+=(y**i)*x[i]
    return sm


#print(fromAny([1,1,1,0],2))
for x in range(40):
    for y in range(40):
        b=[5,7,x,6,9,2,y,1,9]
        if fromAny(b,40)%39==0:
            g=fromAny([y,x],40)
            if int(g**0.5)==g**0.5:
                print(x,y,g,fromAny(b,40))
