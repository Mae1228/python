'''练习2成果包——多彩繁星'''
'''
程序中有效使用random库。
星空背景为黑色，每颗星星（星星用短线代表）绘制时海龟画笔都从原点重新出发进行绘制。
'''

#调用模块
import random
import turtle as t

#画笔设置
t.speed(10)
t.penup()
t.goto(-300, -300)
t.pendown()

#绘制星空背景
t.fillcolor('black')
t.begin_fill()
for i in range(4):
    t.forward(600)
    t.left(90)
t.end_fill()

#绘制多彩星星
for x in range(150):
    #设置随机粗细
    t.pensize(random.randint(1, 3))
    #设置随机颜色
    t.pencolor(random.uniform(0.5, 1), random.uniform(0.5, 1), random.uniform(0.5, 1))
    t.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x, y)
    t.pendown()
    t.forward(1)
    t.penup()
    t.goto(0, 0)

t.hideturtle()
t.done()

