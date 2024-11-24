k=0
for n in range(890_000_000,894_728_061+1):
    ost=n%4
    if ost==0 or ost==1:
        r=2*n+ost
    elif ost==2 or ost==3:
        r=4*n+ost
    if 1_789_456_123>=r>=1_000_000_000:
        #print(n,r)
        k+=1
        #break
    if n%10000000==0:
        print('!',k)
print(k)
#894_728_061,250_000_002
#447_364_031,499_999_999
#296046047
#7 25
