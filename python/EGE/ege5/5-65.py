for i in range(100,1000):
    si=str(i)
    if sorted([int(si[0])+int(si[1]),int(si[1])+int(si[2])],reverse=True) == [15,7]:
        print(i)
