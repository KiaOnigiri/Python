xs, ys, zs, R = [int(x) for x in input().split()]

xp,yp,zp = [int(x) for x in input().split()]

N = int(input())

cords = []
h=0
lelelele=[]
for _ in range(N):
    lelelele.append([int(x) for x in input().split()])
for o in lelelele:
    if h==1:
        break
    if xs == xp and ys == yp and zs == zp and h==0:
        print(len(cords)+2)
        h=1
        break
    elif xs > R or ys > R or zs > R and h==0:
        print(len(cords))
        h=1
        break
    a,b,c = o[0],o[1],o[2]
    j=abs(min(a,b,c))
    j1=max(a,b,c)
    j2=max(j,j1)
    xs1=xs
    ys1=ys
    zs1=zs
    for i in range(1,j2+1):
        xs = a*(i/j2)+xs1
        ys = b*(i/j2)+ys1
        zs = c*(i/j2)+zs1
        if xs == xp and ys == yp and zs == zp and h==0:
            print(len(cords)+2)
            h=1
            break
        elif xs > R or ys > R or zs > R and h==0:
            print(len(cords))
            h=1
            break
        if xs==int(xs) and ys==int(ys) and zs==int(zs):
            cords.append([xs,ys,zs])
if h==0:
    print(len(cords))
