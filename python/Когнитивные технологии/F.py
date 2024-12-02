def pro(l,r):
    p=1
    for i in range(l-1,r):
        p*=a[i]%(10**9+7)
    return p%(10**9+7)
def min_del(x):
    b=[]
    for y in range(3,int(x**0.5)+1,2):
        if x%y==0:
            if y%2!=0:
                return y
    for y in range(2,int(x**0.5)+1):
        if x%y==0:
            if (x//y)%2!=0:
                return x//y
    if x%2!=0:
        return x
    else:
        return 1
    
def dels(l,r):
    for i in range(l-1,r):
        a[i]//=min_del(a[i])
   
b=[]
t=int(input())
for _ in range(t):
    n=int(input())
    a=input().split()
    a=[int(x) for x in a]
    m=int(input())
    for i in range(m):
        c=input().split()
        if c[0]=='?':
            b.append(pro(int(c[1]),int(c[2])))
        elif c[0]=='/':
            dels(int(c[1]),int(c[2]))
        elif c[0]=='=':
            a[int(c[1])-1]=int(c[2])
for x in b:
    print(x)
#print(min_del(72))
