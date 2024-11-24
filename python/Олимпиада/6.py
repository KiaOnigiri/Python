n=int(input())
m=int(input())
b=[]
for i in range(n):
    b.append(int(input()))
g=[]
for uzel in range(n):
    g1=0
    if uzel==0:
        for i in range(m+1):
            g1+=b[i]
        for i in range(n-m-1):
            g1+=b[i+m+1]*(i+m+2)
    elif uzel==1:
        for i in range(m*2+1):
            g1+=b[i]
        for i in range(n-(m*2+1)):
            g1+=b[i+m+2]*(i+m+3)
    elif uzel==n-1:
        for i in range(n-m-1):
            g1+=b[i]*(i+1)
        for i in range(m+1):
            g1+=b[-1*(i+1)]
    elif uzel==n-2:
        for i in range(n-(m*2+1)):
            g1+=b[i]*(i+1)
        for i in range(m*2+1):
            g1+=b[-1*(i+1)]
    else:
        for i in range(1,uzel-m):
            g1+=b[i-1]*(i)
        for i in range(uzel-m,uzel+m+1):
            g1+=b[i-1]
        for i in range(uzel+m+1,n+1):
            g1+=b[i-1]*(i)
    g.append([g1,uzel+1])
f=sorted(g, key=lambda x: x[0])
print(f[0][1])
