for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f=(((not(x)) and (not(y))) or (y and w))==(y and z and (not(w)) and (not(x)))
                if f:
                    print(x,y,z,w)
