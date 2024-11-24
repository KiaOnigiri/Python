for i in range(1000,9999+1):
    s1=int(str(i)[0])+int(str(i)[1])
    s2=int(str(i)[2])+int(str(i)[3])
    if sorted([s1,s2])==[12,14]:
        print(i,s1,s2)
