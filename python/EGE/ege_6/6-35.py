from turtle import *
tracer(2)
m=10
x,y=0,0
for i in range(13):
    x+=6;y+=3
    goto(x*m,y*m)
    x+=-6;y+=2
    goto(x*m,y*m)
    x+=-4;y+=-1
    goto(x*m,y*m)
    x+=4;y+=-4
    goto(x*m,y*m)
up()
color("red")
for x in range(-10,9+1):
    for y in range(-10,15+1):
        goto(x*m,y*m)
        dot(3)
