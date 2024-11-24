import random
n=10
a=[random.randint(10,99) for x in range(n)]
print(a)
k=-1000
x1=0
x2=0
for i in range(len(a)-1):
    if abs(a[i+1]-a[i])>k:
        k=abs(a[i+1]-a[i])
        x1=a[i+1]
        x2=a[i]
x1,x2=min(x1,x2),max(x1,x2)
print('{}-{}={}'.format(x2,x1,k))

        
