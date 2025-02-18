m=int(input())
c=input()
sm=sum([int(x) for x in c])
if sm%3!=0:
    print(-1)
else:
    idx=[i for i in range(len(c)) if int(c[i])%2==0]
    if idx:
        print(m-max(idx)-1)
    else:
        print(-1)
