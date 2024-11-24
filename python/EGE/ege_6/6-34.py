from turtle import *
tracer(2)
m=10
x,y=0,0
for i in range(5):
    x+=6;y+=8
    goto(x*m,y*m)
    x+=-8;y+=4
    goto(x*m,y*m)
    x+=2;y+=-12
    goto(x*m,y*m)
up()
color("red")
for x in range(-10,9+1):
    for y in range(-10,15+1):
        goto(x*m,y*m)
        dot(3)
