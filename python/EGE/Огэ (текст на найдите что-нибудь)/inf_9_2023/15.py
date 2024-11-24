n=int(input())
b=[]
for i in range(n):
    b.append(int(input()))
k=0
for x in b:
    if x%4==0 and x%7!=0:
        k+=1
print(k)
