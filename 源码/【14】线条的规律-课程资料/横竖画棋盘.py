''''''
import turtle as t
t.speed(10)
for x in range(0,181,10):
    t.goto(x,0)
    t.pendown()
    t.goto(x,-180)
    t.penup()
    t.goto(0,-x)
    t.pendown()
    t.goto(180,-x)
    t.penup()
t.hideturtle()
t.done()
