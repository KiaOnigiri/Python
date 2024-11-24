n=int(input())
x=0
y=0
k=0
for i in range(n):
    a=sum([int(x,16) for x in input()])%5
    if a==0:
        k+=1    
print(k)
