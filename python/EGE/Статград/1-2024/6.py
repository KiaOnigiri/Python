from turtle import *
tracer(2)
right(90)
m=20
for i in range(4):
    for j in range(4):
        forward(6*m)
        right(90)
    forward(10*m)
    right(90)
    forward(3*m)
up()
color('green')
for x in range(-15,10):
    for y in range(-15,10):
        goto(x*m,y*m)
        dot(4)
#36
