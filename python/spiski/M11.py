import random
n=10
a=[random.randint(-9,9) for x in range (n)]
print(a)
k=0
s=0
for i in range(len(a)):
    if a[i] <0:
        k=i
        break
for i in range(k+1,len(a),1):   
    s+=abs(a[i])
print(s)
