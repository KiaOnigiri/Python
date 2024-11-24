def F(x,y,z):
    f=(x<=(not z)) and (y<=x)
    return f


for x in range(2):
    for y in range(2):
        for z in range(2):
            if F(x,y,z):
                print(x,y,z)
