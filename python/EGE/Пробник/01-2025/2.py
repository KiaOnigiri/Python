print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f=(not((((not x) or y) and (not w))) or (not(z and (not(y and w)))))
                if not f:
                    print(w,x,y,z,f)
