from turtle import *
tracer(2)
x,y=0,0
m=20
for i in range(7):
    x+=6;y+=-9
    goto(x*m,y*m)
    x+=-6;y+=2
    goto(x*m,y*m)
    x+=12;y+=3
    goto(x*m,y*m)
up()
color('red')
for x in range(-15,15+1):
    for y in range(-15,15+1):
        goto(x*m,y*m)
        dot(3)
#43
