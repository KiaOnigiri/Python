r = [int(i) for i in input().strip()]
k=0
s=0
for g in range(len(r)):
    k+=1
    s+=r[g]
print(s)
print(k)
