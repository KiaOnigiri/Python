a=int(input())
b=int(input())
c=int(input())
x=int(input())
y=int(input())
z=int(input())
ka=a*60*60*24
kb=b*60*24
kc=c*24
print(min(ka//x,kb//y,kc//z))
