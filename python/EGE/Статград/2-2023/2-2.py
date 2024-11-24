def F(u,w,x,y,z):
    f=((x<=y)and(z==(not w)))<=(u==(x or z))
    f=bool(f)
    return f


for u in range(2):
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    if not F(u,w,x,y,z):
                        print(w,z,y,x,u)
