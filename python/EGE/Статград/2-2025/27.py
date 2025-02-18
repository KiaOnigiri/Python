from turtle import *
def minrad(claster):        
    smx2=[]       
    for x in claster:
        mx=0
        for y in claster:
            if ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5>mx:
                mx=((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5
        smx2.append([x,mx])
    smx2.sort(key=lambda x: [x[1],x[0]])
    #print(smx2[:3])
    return smx2[0][1]

    
f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Статград/2-2025/Доп/27B.txt')
s=f.read().splitlines()
s=[[float(y) for y in x.split()] for x in s]
#print(s[:5])
'''
tracer(1000)
m=32
screensize(10000,10000)
for xline in range(-10,10):
    up()
    goto(xline*m,-10*m)
    down()
    goto(xline*m,10*m)
    goto(xline*m,0)
    write(f'{xline}')
for yline in range(-10,10):
    up()
    goto(-10*m,yline*m)
    down()
    goto(10*m,yline*m)
    goto(0,yline*m)
    write(f'{yline}')
color('blue')
up()
goto(-10*m,0)
down()
goto(10*m,0)
up()
goto(0*m,-10*m)
down()
goto(0,10*m)
up()
color('red')

for x in s:
    goto(x[0]*m,x[1]*m)
    dot(8)
'''
cl1=[]
cl2=[]
cl3=[]
cl4=[]
cl5=[]
for x in s:
    if -1<=x[0]<=3 and 5.5<x[1]<=9:
        cl1.append(x)
    if 4<=x[0]<=6 and 6<=x[1]<=8:
        cl2.append(x)
    if 2<=x[0]<=4 and 2.5<=x[1]<=5.5:
        cl3.append(x)
    if -1<=x[0]<=2 and 2<=x[1]<=4:
        cl4.append(x)
    if -5<=x[0]<=-1 and -1<=x[1]<=3:
        cl5.append(x)
print(len(cl1),len(cl2),len(cl3),len(cl4),len(cl5),len(s))
#cl1 - исключен
lst=[]
for n,claster in enumerate((cl2,cl3,cl4,cl5),2):
    #print(n,minrad(claster))
    lst.append(minrad(claster))

print(10000*sum(lst)/len(lst))
#10001

