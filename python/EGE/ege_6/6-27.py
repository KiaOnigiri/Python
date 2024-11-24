from turtle import *
tracer(2)
m=15
left(90)
for i in range(7):
    right(90)
    forward(4*m)
    for j in range(2):
        left(90)
        forward(4*m)
up()
color('red')
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3)
