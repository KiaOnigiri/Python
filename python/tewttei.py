def newmax(tri,x):
    if min(tri)<x:
        tri[tri.index(min(tri))]=x
    return sorted(tri,reverse=True)


f=open('C:/python/EGE/Статград/1-2024/Faily_IN11_06022024_/27-B.txt')
s=f.read().splitlines()
s=[int(x) for x in s]
n=s[0]
s=s[1:]
ost=dict()
for i in range(102):
    ost[i]=[0,0,0]
for x in s:
    ost[x%102]=newmax(ost[x%102],x)
mx=0
abc=[]
for i1 in range(102):
    for i2 in range(i1,102):
        for i3 in range(i2,102):
            if (i1+i2+i3)%102==0:
                frst=max(ost[i1])
                ost[i1].remove(frst)
                scnd=max(ost[i2])
                ost[i2].remove(scnd)
                thrd=max(ost[i3])
                ost[i3].remove(thrd)
                troyka=frst+scnd+thrd
                #mx=max(mx,troyka)
                if troyka>mx:
                    mx=troyka
                    abc=[frst,scnd,thrd,frst%102,scnd%102,thrd%102]
                    #print(mx,abc)
                ost[i1].append(frst)
                ost[i2].append(scnd)
                ost[i3].append(thrd)
print(mx,abc)              
