for N in range(1,300000):
    s1=sum([int(x) for x in str(N) if int(x)%2==0])
    s2=sum([int(str(N)[i]) for i in range(len(str(N))) if i%2==0])
    R=abs(s1-s2)
    if R==27:
        print(N,R)
