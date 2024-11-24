x=int(input())
b=list(map(int, input().split()))
y=int(input())
sm=sum(b)
c=[]
for i in range(y):
    v=list(map(int, input().split()))
    if v[0]==1:
        sm+=v[2]-b[v[1]-1]
        b[v[1]-1]=v[2]
    if v[0]==2:
        b=b[-v[1]:]+b[:-v[1]]
    #print(b)
    c.append(sm)
print(*c,sep='\n')

