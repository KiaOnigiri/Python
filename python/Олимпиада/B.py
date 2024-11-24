def postr(a):
    imax=-1
    kimax=0
    for i in range(h):
        ki=0
        for j in range(w):
            if a[i][j]==1:
                ki+=1
        if ki>kimax:
            kimax=ki
            imax=i
    return [imax,kimax]



f=open('01.txt')
s=f.read().splitlines()
w,h,n=map(int, s[0].split())
a=[]
for j in range(h):
    a.append([0]*w)
for i in range(1,n+1):
    y,x=map(int, s[i].split())
    'print(x,y)'
    a[x-1][y-1]=1
for z in range(len(a)):
    print(a[z])
stolb=[]
print('---')
jmax=-1
kjmax=0
m=[]
for j in range(w):
    kj=0
    for i in range(h):
        if a[i][j]==1:
            kj+=1
            a[i][j]='!'
    if kj>kjmax:
        kjmax=kj
        jmax=j
    #print([j,kj],postr(a))
    m.append([kj+postr(a)[1],j,postr(a)[0]])
    for i in range(h):
        if a[i][j]=='!':
            a[i][j]=1
#print(m)
print('points={},row={},col={}'.format(max(m)[0],max(m)[2],max(m)[1]))
f.close()
