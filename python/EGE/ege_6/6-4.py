from turtle import *
tracer(2)
left(90)
color('green')
m=20
for i in range(10):
    right(60)
    forward(10*m)
    right(60)
up()
color('purple')
for x in range(-10,10+1):
    for y in range(-10,10+1):
        goto(x*m,y*m)
        dot(2)
#42
