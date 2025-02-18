from turtle import *
lt(90)
tracer(100)
m=10
for i in range(8):
    fd(16*m)
    rt(90)
    fd(22*m)
    rt(90)
up()
fd(5*m)
rt(90)
fd(5*m)
lt(90)
down()
for i in range(9):
    fd(52*m)
    rt(90)
    fd(77*m)
    rt(90)
up()
color('red')
for x in range(-5,30):
    for y in range(-5,30):
        goto(x*m,y*m)
        dot(3)
