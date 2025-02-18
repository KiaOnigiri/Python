points,t=[int(x) for x in input().split()]
c=[]
for _ in range(points):
    x,y=input().split()
    x,y=int(x),int(y)
    c.append((x,y))
b=[]
for _ in range(t):
    #c=[(0,0),(0,5),(5,5),(0,10),(0,5)]
    sec=int(input())
    startsec=sec
    i=0
    x,y=c[0][0],c[0][1]
    while True:
        if c[i][0]==c[i+1][0]:
            r=abs(c[i+1][1]-c[i][1])
        elif c[i][1]==c[i+1][1]:
            r=abs(c[i+1][0]-c[i][0])
        else:
            r=((c[i][0]-c[i+1][0])**2+(c[i][1]-c[i+1][1])**2)**(0.5)
        dx=c[i+1][0]-c[i][0]
        dy=c[i+1][1]-c[i][1]
        if sec-r>0:
            x+=dx
            y+=dy
            sec-=r
        elif sec-r==0:
            x+=dx
            y+=dy
            sec-=r
            break
        else:
            x+=dx*(sec/r)
            y+=dy*(sec/r)
            break
        i+=1
        if i==len(c)-1:
            roundd=startsec-sec
            rounds=startsec//(roundd)
            if startsec%roundd==0:
                if rounds%2==0:
                    x=float(c[0][0])
                    y=float(c[0][1])
                    break
                else:
                    x=float(c[-1][0])
                    y=float(c[-1][1])
                    break
            if rounds%2!=0:
                sec=startsec%roundd
                c=c[::-1]
                x,y=float(c[0][0]),float(c[0][1])
            else:
                sec=startsec%roundd
                x,y=float(c[0][0]),float(c[0][1])
            i=0
    b.append([x,y])
for x in b:
    print(*x)
#30 100
#33 990
