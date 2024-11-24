for A in range(50,80):
    flag=0
    for x in range(-1000,1000):
        for y in range(-1000,1000):
            f=((y<20)<=(x>70))or(not((x<A)<=(y>A)))
            if f==False:
                flag=1
                break
        if flag==1:
            break
    if flag==0:
        print(A)
