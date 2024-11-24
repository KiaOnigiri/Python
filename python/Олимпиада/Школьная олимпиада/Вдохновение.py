n=int(input())
a=int(input())
b=int(input())
c=int(input())
b_norm=b-a
c_norm=c-a
if b_norm<0 or c_norm<0 or (n-c_norm-b_norm-a)<0:
    print(-1)
else:
    print(n-c_norm-b_norm-a)
