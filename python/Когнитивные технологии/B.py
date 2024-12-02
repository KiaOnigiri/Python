kmax=0
ans=[]
for i in range(int(input())):
    k=0
    c=input()
    b=[int(x) for x in input().split()]
    b1=sorted(set(b),reverse=True)
    for j in range(len(b1)):
        curr=b1[j]
        k=sum(map(lambda item: curr>=item, b[b.index(curr):]))
        #for j1 in b[b.index(curr):]:
        #    if curr>=j1:
        #        k+=1
        kmax=max(k,kmax)
        k=0
    ans.append(kmax)
    kmax=0
for ns in ans:
    print(ns)
        
#4 5 6 7 8 9
#4 1 4 5 6 7 4
#1 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 4 4 4 4 4 4 5 5 100
