''''''
import turtle as t
t.speed(10)
# t.pencolor('red')
# t.fillcolor('red')
# t.begin_fill()
# t.circle(2)
# t.end_fill()
t.pencolor('black')
for x in range(-90,91,10):
    t.penup()
    t.goto(x,90)
    t.pendown()
    t.goto(x,-90)
for y in range(90,-91,-10):
    t.penup()
    t.goto(90,y)
    t.pendown()
    t.goto(-90,y)
t.hideturtle()
t.done()