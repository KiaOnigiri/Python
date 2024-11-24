g=int(input())

b=[]
for i in range(g):
    b.append(int(input()))
k=0
for i in range(1,len(b)):
    if b[i-1]<b[i]:
        k+=1
print(k)
