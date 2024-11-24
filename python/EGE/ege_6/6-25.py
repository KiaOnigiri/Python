from turtle import *
tracer(2)
m=10
left(90)
right(90)
for i in range(12):
    forward(9*m)
    right(72)
up()
color("red")
for x in range(-10,8+1):
    for y in range(-5,15+1):
        goto(x*m,y*m)
        dot(3)
