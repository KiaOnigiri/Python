k=0
n=int(input())
x=int(input())
y=int(input())
b=[x,y]
while True:
    if min(b)<=n:
        b.append(int(str(min(b))+str(y)))
        b.append(int(str(min(b))+str(x)))
        b=list(filter(lambda x: x != min(b), b))
        k+=1
    else:
        break
if k==0:
    print('-1')
elif x==0 or y==0:
    print(k-1)
else:
    print(k)
