'''
奔跑的幸运形-工程包
'''

#第一步：导入海龟绘图工具箱和随机数工具箱
import turtle as t
import random 

#第二步：命名绘制窗口，设置背景色

#第三步：绘制终点小红旗
t.color("red")
t.fillcolor("red")
t.penup()
t.goto(200, 0)
t.left(90)
t.pendown()
t.forward(30)
t.begin_fill()
t.forward(40)
t.right(90)
t.forward(40)
t.right(135)
t.forward(40*pow(2,0.5))
t.end_fill()
t.penup()
t.goto(0, 200)
t.hideturtle()

#第四步：添加比赛的图形
#选手入场

#各就各位

#第五步：比赛过程
#比赛开始

#比赛结束
        t.write("待添加的文本", align='center', font=('arial', 30, 'normal'))
        t.write("待添加的文本", align='center', font=('arial', 30, 'normal'))
        t.write("待添加的文本", align='center', font=('arial', 30, 'normal'))

#第六步：停止绘制，使窗口停留
