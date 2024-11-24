def dext(s):
    y=[]
    ns=s
    for i in range(len(s)):
        s=ns[i:]+ns[:i]
        for dex in range(min(s),max(s)+1):
            dex1=dex
            for platform in s:
                if dex>=platform:
                    dex+=1
                else:
                    break
            else:
                y.append([dex1,i+1])
                break
    if y==[]:
        return False
    else:
        return min(y)
            

def f2(n,m,x,y,z,c):  
    d=list('0'*n)
    for i in range(n):
        if 0<=i<=m-1:
            d[i]=c[i]
        else:
            d[i]=((x*d[i-2]+y*d[i-1]+z)%10**9)+1
    return (d)


n=int(input())
f=int(input())
if f==1:
    d=list(map(int, input().split()))
    print(*dext(d))
if f==2:
    m,x,y,z=map(int, input().split())
    c=list(map(int, input().split()))
    print(*dext(f2(n,m,x,y,z,c)))
