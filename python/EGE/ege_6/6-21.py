from turtle import *
tracer(2)
m=10
left(90)
for i in range(7):
    left(60)
    forward(5*m)
    left(120)
    forward(5*m)
up()
color("red")
for x in range(-15,15+1):
    for y in range(-15,15+1):
        goto(x*m,y*m)
        dot(3)
