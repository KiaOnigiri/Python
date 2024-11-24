f=open('26-72.txt')
s=f.read().splitlines()
x,y,n=[int(q) for q in s[0].split()]
s=s[1:]
matrix=[]
for o in range(y):
    matrix.append([0]*x)
for w in s:
    x1,y1=[int(q) for q in w.split()]
    #print(x1,y1)
    matrix[x1-1][y1-1]=1
#for line in matrix:
#    print(*line)
b=[]
k=0
k1=0
mxk=0
p=0
for i in range(len(matrix)):
    for j in range(3,len(matrix[i])):
        if matrix[i][j-1]==0 and matrix[i][j]==0 and matrix[i][j-2]==0 and matrix[i][j-3]==0:
            b.append([i+1,j-2])
            k1+=1
            k+=1
            if mxk<k:
                p=i+1
            mxk=max(mxk,k)
    k=0
print(k1,p)
