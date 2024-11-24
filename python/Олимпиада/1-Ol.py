from statistics import mean
a,c,m,xpr,n=map(int, input().split())
b=[]
for i in range(n):
    x=(a*xpr+c)%m
    b.append(x)
    xpr=x
print('%.4f'%(mean(b)))
    
