from random import randint
from time import *
t1=time()
def stolbec(cell,column):
    k=0
    for i in range(len(a)):
        if a[i][column]==cell:
            k+=1
    return k
    

n=5
f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Статград/2-2025/Доп/09.txt')
a=[[int(x) for x in line.split()] for line in f.read().splitlines()]
#a=[[randint(10,19) for x in range(n)] for line in range(n)]
#for line in a:
#    print(*line)
f.close()
#print(a[:3])

k=0 
for line in a:
    interest=0
    sr=sum(line)/len(line)
    for i,cell in enumerate(line,0):
        if line.count(cell)==1 and cell>sr and stolbec(cell,i)>=331:
            interest+=1
    if interest==1:
        print(line,cell)
        k+=1
        if k==10:
            break
print(k)
t2=time()
print(t2-t1)
'''
for i,x in enumerate([2,3,4],0):
    print(i,x)
'''
