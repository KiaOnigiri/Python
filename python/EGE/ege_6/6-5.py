from turtle import *
tracer(2)
left(90)
color('green')
m=20
for i in range(8):
    forward(12*m)
    right(90)
up()
color('purple')
for x in range(-12,12+1):
    for y in range(-12,12+1):
        goto(x*m,y*m)
        dot(3)
#121
