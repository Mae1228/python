import turtle
import random#导入random库
t=turtle.Pen()
turtle.bgcolor('black')
t.pencolor('yellow')
for x in range(30):
    t.penup()
    t.goto(random.randint(-350,350),random.randint(-200,200))
    t.pendown()
    dens=12
    snowsize=x
    for j in range(dens):
        t.forward(snowsize)
        t.backward(snowsize)
        t.right(360/dens)
turtle.done()











