def centroid(cl):
    sr_ar=[sum([star[0] for star in cl])/len(cl),sum([star[1] for star in cl])/len(cl)]
    kmin=100000
    for star in cl:
        r=((star[0]-sr_ar[0])**2+(star[1]-sr_ar[1])**2)**0.5
        if r<kmin:
            kmin=r
            cntr=star
    return cntr
        
from turtle import *
f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Статград/1-2025/Доп/27B.txt')
s=f.read().splitlines()
s=[[float(y) for y in x.split()] for x in s]
'''
m=45
tracer(1000)
color('grey')
for x in range(-20,20):
    up()
    goto(x*m,-20*m)
    down()
    goto(x*m,20*m)
for y in range(-20,20):
    up()
    goto(-20*m,y*m)
    down()
    goto(20*m,y*m)
color('black')
up()
goto(0*m,-20*m)
down()
goto(0*m,20*m)
up()
goto(-20*m,0*m)
down()
goto(20*m,0*m)
up()
for star in s:
    goto(star[0]*m,star[1]*m)
    dot(3)
'''
#cl1=[]
#for star in s:
#    if 3<=star[0]<=7 and -3<=star[1]<=1:
#        cl1.append(star)
cl2=[]
for star in s:
    if -3<=star[0]<=1 and -2<=star[1]<=2:
        cl2.append(star)
cl3=[]
for star in s:
    if 3<=star[0]<=7 and 1<=star[1]<=5:
        cl3.append(star)
cl4=[]
for star in s:
    if -1<=star[0]<=3 and 3<=star[1]<=6:
        cl4.append(star)
cl5=[]
for star in s:
    if 3<=star[0]<=8 and 5<=star[1]<=8:
        cl5.append(star)
print(len(cl2),len(cl3),len(cl4),len(cl5),len(s))
cntr2=centroid(cl2)
cntr3=centroid(cl3)
cntr4=centroid(cl4)
cntr5=centroid(cl5)
print((cntr2[0]+cntr3[0]+cntr4[0]+cntr5[0])/4*10000,(cntr2[1]+cntr3[1]+cntr4[1]+cntr5[1])/4*10000)
