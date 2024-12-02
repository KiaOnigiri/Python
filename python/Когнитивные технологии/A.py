c=[]
for i in range(int(input())):
    b=set()
    for j in range(int(input())):
        j1=input()
        for x in j1:
            b.add(x)
    c.append(len(b))
for mm in c:
    print(mm)
