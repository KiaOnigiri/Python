P=range(3,43+1)
Q=range(18,91+1)
R=range(72,115+1)
#A=range(44,71+1)
for x in range(2,117):
    t=(x in Q)<=((not (x in P))<=(((not(x in R))and(not(x in [])))<=(not(x in Q))))
    print(x,t)
#27
