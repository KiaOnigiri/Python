from turtle import *

def findEnd(x):
    for smth in p:
        if x==smth[0]:
            return smth[3]
def podval(secs):
    b=[]
    for i in range(1,secs+1):
        k=0
        for smth in p:
            if smth[4]<=i<=smth[3]:
                k+=1
        b.append(k)
    return b
    

f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege_22/22-3.txt')
s=f.read().splitlines()
s=s[1:]
s=[line.split() for line in s]
p=[]
for line in s:
    z=line[2:]
    zID=[]
    if len(z)==1:
        zID.append(int(line[2]))
    else:
        for x in z:
            c=''
            for y in x:
                if y.isdigit(): c+=y
            zID.append(int(c))
    p.append([int(line[0]),int(line[1]),zID])
p.sort(key=lambda x: x[2])
#print(p)

for i in range(len(p)):
    if p[i][2][0]==0:
        p[i].append(p[i][1])
        p[i].append(1)
    else:
        ends=[]
        for smth in p[i][2]:
            ends.append(findEnd(smth))
        p[i].append(p[i][1]+max(ends))
        p[i].append(p[i][3]-p[i][1]+1)
print(p)
print(podval(40))
#0-id 1-executetime 2-ids 3-end 4-begin
tracer(2)
m=20
screensize(10000,10000)
for xline in range(-1,40+1):
    up()
    goto(xline*m,-3*m)
    down()
    goto(xline*m,10*m)
for yline in range(-3,10+1):
    up()
    goto(-1*m,yline*m)
    down()
    goto(40*m,yline*m)
up()
for cycle in range(1,40+1):
    goto(cycle*m-13,9.1*m)
    write(cycle)
p=list(reversed(p))
for smth in range(len(p)):
    goto(-0.8*m,smth*m-57)
    write(p[smth][0])
    for i in range(p[smth][4],p[smth][3]+1):
        goto(i*m-11,smth*m-51)
        color("red")
        dot(12)
        color("black")
goto(-10000,-10000)
dot(1)
