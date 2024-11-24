from turtle import *
tracer(2)
left(90)
color('green')
m=20
for i in range(15):
    forward(4*m)
    right(60)
up()
color('purple')
for x in range(1,15+1):
    for y in range(1,15+1):
        goto(x*m,y*m)
        dot(4)
#28
