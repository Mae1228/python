import turtle as t
import random
t.bgcolor('black')
t.pencolor('yellow')

def move():     #移动画笔
    t.penup()
    x=random.randint(-500,500)
    y=random.randint(-300,300)
    t.goto(x,y)
    t.pendown()#抬笔落笔防止移动中出现不必要的痕迹

def fun1():     #画五角星
    for x in range(5):
        t.fd(50)
        t.right(144)

for x in range(50):
    fun1()
    move()
t.done()#使画布停留不消失









