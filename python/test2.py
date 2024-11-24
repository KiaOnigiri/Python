def onlynumbers(x):
    x=[str(j) for j in x]
    x1=[]
    for i in x:
        if i.isdigit()==True:
            x1.append(int(i))
    return x1


n=int(input())
b=[]
k=0
for i in range(n):
    b.append(str(input()))
for j in b:
    if sum(onlynumbers(j))%8==6:
        k+=1
print(k)
