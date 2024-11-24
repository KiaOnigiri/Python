from turtle import *
tracer(2)
m=10
left(90)
forward(9*m)
right(90)
for i in range(2):
    forward(3*m)
    right(90)
    forward(3*m)
    right(270)
for i in range(2):
    forward(3*m)
    right(90)
forward(9*m)
up()
color("red")
for x in range(0,15+1):
    for y in range(0,15+1):
        goto(x*m,y*m)
        dot(3)
