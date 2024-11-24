P=range(15,40+1)
Q=range(21,63+1)
A=[]
for x in range(14,64+1):
    #for a2 in range()
    f=(x in P)<=(((x in Q)and(not(x in A)))<=(not(x in P)))
    if not f:
        print(x)
    
