def F(x,y,z,w):
    f=((x<=y)and(y<=w))or(z==(x or y))
    f=bool(f)
    return f


for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f=F(x,y,z,w)
                if not f:
                    print(x,y,z,w,f)
