bb=[]
for i in range(int(input())):
    a,b=input().split()
    a=int(a)
    b=int(b)
    g=0
    if a==0 and b==0:
        g=1
    elif a==1 and b==0:
        g=1
    elif a==2 and b==0:
        g=1
    elif a>=b and a not in [0,1,2]:
        g=1
    if g==1:
        bb.append('YES')
    else:
        bb.append('NO')
for x in bb:
    print(x)
