'''秘密星轨-成果包'''

#调用模块
import turtle as t
import random

#画笔设置
# t.speed(100)
t.penup()
t.goto(-400, -400)
t.pendown()

#绘制星空背景
t.fillcolor('black')
t.begin_fill()
for i in range(4):
    t.forward(800)
    t.left(90)
t.end_fill()

#回到原点
t.penup()
t.goto(0,0)

#绘制星轨
t.pencolor("cyan")
for x in range(150):
    #随机获取圆弧半径
    r = random.randint(1, 400)
    #转到对应角度
    t.right(random.randint(0, 360))
    #移动到画弧的起点
    t.forward(r)
    #转到绘画角度
    t.left(90)
    #画弧
    t.pendown()
    t.circle(r, 60)
    #回到原点
    t.penup()
    t.goto(0, 0)
    
t.hideturtle()
t.done()

