from turtle import *
x,y=0,0
m=20
tracer(2)
for i in range(3):
    x+=-6;y+=9
    goto(x*m,y*m)
    x+=6;y+=-2
    goto(x*m,y*m)
    x+=-3;y+=-6
    goto(x*m,y*m)
up()
color('red')
for x in range(-10,10+1):
    for y in range(-10,10+1):
        goto(x*m,y*m)
        dot(3)
#7+4*8+5
