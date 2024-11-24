from itertools import permutations
N,X,Y=4,3,7
b=[4,10,7,12]
'''
N=int(input())
X=int(input())
Y=int(input())
b=[]
for i in range(N):
    b.append(int(input())
'''
k=0
p=list(permutations(b))
print(p)
if N*Y<=sum(b):
    for v in p:
        oil=0
        flag=True
        for tank in v:
            oil+=Y
            if tank>oil:
                ost=tank-oil
                oil=0
            else:
                oil-=tank
                ost=0
            #print('Oil={}, Tanker={}, Ostatok={}'.format(oil,tank,ost))
            if ost>X:
                flag=False
                break
        #print('----')
        if flag and oil==0:
            print(v)
            k+=1
print(k)

