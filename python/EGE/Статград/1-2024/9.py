def checkstolb(x,y):
    k=0
    for i in range(len(s)):
        if s[i][y]==s[x][y]:
            k+=1
    return k
    


f=open('9.txt')
s=f.read().splitlines()
s=[[int(y) for y in x.split()] for x in s]
#print(s[:5])
k=0
for i in range(len(s)):
    if i%1000==0:
        print('!')
    h=0
    for j in range(len(s[i])):
        if s[i].count(s[i][j])==1 and checkstolb(i,j)>150:
            h+=1
    if h>=5:
        k+=1
print(k)
