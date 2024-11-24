from turtle import *
tracer(2)
rt(90)
m=10
for i in range(2):
    fd(17*m)
    lt(90)
    fd(10*m)
    lt(90)
up()
backward(4*m)
rt(90)
backward(3*m)
lt(90)
down()
for i in range(2):
    fd(40*m)
    rt(90)
    fd(10*m)
    rt(90)

up()
color('red')
for x in range(-10,13):
    for y in range(-40,5):
        goto(x*m,y*m)
        dot(2)
