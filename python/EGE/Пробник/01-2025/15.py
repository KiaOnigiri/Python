for A in range(0,100):
    g=0
    for x in range(1,70):
        for y in range(1,405):
            f=(((x-3*y)<A)or(y>400)or(x>56))
            if not f:
                g=1
    if g==0:
        print(A)
        break
