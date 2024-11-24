import random
n=10
a=[random.randint(10,99) for x in range (n)]
print(a)
for i in range(1,len(a),2):
    a[i-1],a[i]=a[i],a[i-1]
print(a)
