k=int(input())
b=[]
for i in range(k):
    b.append(int(input()))
print(sum(b)-min(b)+1)
