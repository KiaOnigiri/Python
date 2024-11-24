for p in range(9,20):
    for x in range(1,p):
        for y in range(0,p):
            for z in range(1,p):
                for w in range(1,p):
                    c1=f'{z}{x}{y}{x}4'
                    c2=f'{x}{y}658'
                    c3=f'{w}{z}{x}73'
                    if int(c1,p)+int(c2,p)==int(c3,p):
                        print(p,x,y,z,w)
print(int(str(1467),9))
