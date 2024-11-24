n,m,z=5,7,2
Map=[[1,2],[2,3],[3,4],[4,5],[3,5],[2,5],[1,5]]
c=2
Work=[4,5]
sosedi=dict()
for i in range(1,n+1):
    sosedi[i]=[]
for x in Map:
    sosedi[x[0]].append(x[1])
    sosedi[x[1]].append(x[0])
print(sosedi)
Rest=list(set(i for i in range(1,n+1))-set(Work))
isNew=True
while isNew:
    isNew=False
    for x in Rest:
        k=0
        for y in sosedi[x]:
            if y in Work:
                k+=1
        if k>=z:
            Work.append(x)
            Rest.remove(x)
            print(x,Rest)
            isNew=True
print(Work,Rest)
