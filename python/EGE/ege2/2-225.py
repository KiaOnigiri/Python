def F(x,y,z,w):
    f=(y or x) == ((y <= w) or (not z))
    f=bool(f)
    return f

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f=F(x,y,z,w)
                if not f:
                    print(x,y,z,w,f)
