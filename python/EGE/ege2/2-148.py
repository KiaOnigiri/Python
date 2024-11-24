def F(x,y,z):
    f=(y<=z) and (x<=y)
    f=bool(f)
    return f


for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x,y,z,F(x,y,z))
