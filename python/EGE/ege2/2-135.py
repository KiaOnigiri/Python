def F(x,y,z,w):
    f=(not y) and x and ((not z) or w)
    return f
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if F(x,y,z,w):
                    print(x,y,z,w)
