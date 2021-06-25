'''海龟螺旋线-练习包'''

#调用模块
# import turtle
import turtle as t
# from turtle import pensize, forward

#画条线小例
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
#隐藏画笔
t.hideturtle()
#阻止界面自动关闭(改为点击关闭)
t.done()

#进阶练习：正方形作图练习
#画笔设置
t.pensize(2)
t.speed(10)
t.pencolor("red")
#前进再右转的代码重复四次实现正方形的绘制
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
#优化练习:用循环结构实现正方形的绘制
for x in range(4):
    t.forward(50)
    t.right(90)
#隐藏画笔
t.hideturtle()
#阻止界面自动关闭(改为点击关闭)
t.done()

#绘制螺旋线练习关键步骤拆解：步长设置
for x in range(2, 10, 3):
    print(x)
    t.forward(x)
    t.right(90)
#隐藏画笔
t.hideturtle()
#阻止界面自动关闭(改为点击关闭)
t.done()
