print('X Y Z W F')
for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            for w in [0,1]:
                ans=(x==(y<=z))and(y==(not(z<=w)))
                print(x,y,z,w,ans)
