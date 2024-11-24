def nod(x,y):
    while x!=y:
            if x>y:
                x-=y
            else:
                y-=x
    return x


f=open('C:/python/EGE/ege27/27-data/36/27-36a.txt')
s=f.read().splitlines()
s=s[1:]
s=[[int(y) for y in x.split()] for x in s]
print(s[:5])
b=[]
k=0
for x in s:
    x01=nod(x[0],x[1])
    x02=nod(x[0],x[2])
    x21=nod(x[2],x[1])
    x01min02=abs(x01-x02)
    x01min21=abs(x01-x21)
    x02min21=abs(x02-x21)
    b.append(x01min02)
    b.append(x01min21)
    b.append(x02min21)
    k+=max(x01,x02,x21)
print(sorted(b).count(1),k)
#110
#519880
