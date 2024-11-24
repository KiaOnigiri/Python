from turtle import *
x,y=0,0
m=20
tracer(2)
for i in range(15):
    x+=10;y+=10
    goto(x*m,y*m)
    x+=3;y+=-6
    goto(x*m,y*m)
    x+=-9;y+=3
    goto(x*m,y*m)
up()
color('red')
for x in range(0,15+1):
    for y in range(0,15+1):
        goto(x*m,y*m)
        dot(3)
