from turtle import *
tracer(2)
left(90)
m=8
for i in range(2):
    fd(17*m)
    lt(90)
    fd(10*m)
    lt(90)
up()
bk(4*m)
rt(90)
bk(3*m)
lt(90)
down()
for i in range(2):
    fd(40*m)
    rt(90)
    fd(10*m)
    rt(90)
up()
color('red')
for x in range(-10,30+1):
    for y in range(-10,40+1):
        goto(x*m,y*m)
        dot(3)
