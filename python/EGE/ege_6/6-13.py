from turtle import *
tracer(2)
m=2
left(90)
forward(200*m)
for i in range(4):
    right(90)
    forward(100*m)
up()
color('red')
for x in range(0,1000+1):
    for y in range(0,1000+1):
        goto(x*m,y*m)
        dot(2)
#10301
