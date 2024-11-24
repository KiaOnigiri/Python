from turtle import *
tracer(2)
m=15
left(90)
for i in range(40):
    left(45)
    forward(6*m)
    right(90)
up()
color("red")
for x in range(-5,10+1):
    for y in range(-5,15+1):
        goto(x*m,y*m)
        dot(3)
