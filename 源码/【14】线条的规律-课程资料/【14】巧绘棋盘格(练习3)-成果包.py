'''巧绘棋盘格'''
#调用turtle模块
import turtle as t
#绘制棋盘格的竖线，通过设置步长去改变每条竖线的起/终点坐标
for x in range(0, 181, 10):
    t.penup()
    t.goto(x, 0)
    t.pendown()
    t.goto(x, 180) 
#绘制棋盘格的横线，通过设置步长去改变每条横线的起/终点坐标
for x in range(0, 181, 10):
    t.penup()
    t.goto(0, x)
    t.pendown()
    t.goto(180, x)
t.hideturtle()
t.done()



