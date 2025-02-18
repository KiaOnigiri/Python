from turtle import *
def distance(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5
def near(cl):
    mn=10000000
    for smth in cl:
        sm=0
        for smth2 in cl:
            sm+=distance(smth,smth2)
        if mn>sm:
            mn=sm
            nearest=smth
    return nearest
#screensize(5000,5000)
f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Пробник/01-2025/27-b.txt')
s=f.read().splitlines()
s=s[1:]
s=[[float(y) for y in x.replace(',','.').split()] for x in s]
'''
tracer(1000)
up()
for smthh in range(-20,20):
    goto(smthh*30,-20*30)
    down()
    goto(smthh*30,20*30)
    up()
for smthh in range(-20,20):
    goto(-20*30,smthh*30)
    down()
    goto(20*30,smthh*30)
    up()
color('white')
goto(-20.1*30,0)
down()
goto(20.1*30,0)
up()
goto(0,-20*30)
down()
goto(0,20*30)
up()
color('red')
for smth in s:
    goto(smth[0]*30,smth[1]*30)
    dot(3)
'''

cl1=[]
cl2=[]
cl3=[]
for smth in s:
    if -6<=smth[0]<=0 and -2<=smth[1]<=4:
        cl1.append(smth)
    elif 0<=smth[0]<=7 and 2<=smth[1]<=7:
        cl2.append(smth)
    else:
        cl3.append(smth)
nearest=near(cl1)
nearestt=near(cl2)
nearesttt=near(cl3)
print(nearesttt,nearestt,nearest)
print(10000*(nearestt[0]+nearest[0]+nearesttt[0])/3,10000*(nearestt[1]+nearest[1]+nearesttt[1])/3)
#print(len(cl1),len(cl2),len(s))
