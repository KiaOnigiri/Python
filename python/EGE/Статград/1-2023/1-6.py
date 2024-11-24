from turtle import *
left(90)
tracer(2)
m=15
for i in range(8):
    right(45)
    forward(8*m)
up()
color('green')
for x in range(0,20):
    for y in range(-20,10):
        goto(x*m,y*m)
        dot(4)
