import turtle
turtle.speed(10)
# turtle.width(10)#画笔粗细（正值）
turtle.pensize(10)
color_pool=["blue","black","red","yellow","green"]
s=0
for i in range(3):
    turtle.penup()
    turtle.goto(s, 0)
    turtle.pendown()
    turtle.color(color_pool[i])
    turtle.circle(50)
    s+=120
s1=60
for i in range(3,len(color_pool)):
    turtle.penup()
    turtle.goto(s1, -50)
    turtle.pendown()
    turtle.color(color_pool[i])
    turtle.circle(50)
    s1+=120

turtle.done()