from turtle import *
tracer(2)
left(90)
color('green')
m=20
for i in range(36):
    right(60)
    forward(1*m)
    right(60)
    forward(1*m)
    right(270)
up()
color('purple')
for x in range(-1,1+1):
    for y in range(-1,1+1):
        goto(x*m,y*m)
        dot(3)
#24
