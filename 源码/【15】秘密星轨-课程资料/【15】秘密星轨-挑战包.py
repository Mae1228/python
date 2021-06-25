'''秘密星轨-挑战包'''
'''stamp:标记修改点,本文共有1个标记'''

#调用模块
import turtle as t
import random
import math 

#画笔设置
t.speed(100)
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
t.goto(0, 0)

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

#stamp1:绘制元素 这里绘制了一条圆心在背景中心，半径为800，度数为60的圆弧
t.pencolor("green")
t.seth(0)  # 设置朝向为默认的向右
t.goto(-400, -120)  # 绘制起点
t.pendown()
t.fillcolor('green')
t.begin_fill()
t.right(30)  
t.circle(800, 60)  
t.seth(270)  # 设置朝向向下
t.forward(280)
t.seth(180)  # 设置朝向向左
t.forward(800)
t.seth(90)  # 设置朝向向上
t.forward(280)
t.end_fill()

t.hideturtle()
t.done()
