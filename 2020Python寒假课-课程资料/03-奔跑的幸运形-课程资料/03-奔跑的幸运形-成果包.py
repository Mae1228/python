'''
奔跑的幸运形-成果包
'''

#第一步：导入海龟绘图工具箱和随机数工具箱
import turtle as t
import random 

#第二步：命名绘制窗口，设置背景色
t.title("奔跑的幸运形")
t.bgcolor("pink")

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
t1 = t.Pen()
t1.color("green")
t1.shape('circle')
t2 = t.Pen()
t2.color("blue")
t2.shape('square')
t3 = t.Pen()
t3.color("purple")
t3.shape('triangle')
#各就各位
t1.penup()
t1.goto(-300, 100)
t2.penup()
t2.goto(-300, 0)
t3.penup()
t3.goto(-300, -100)

#第五步：开始赛跑
#比赛开始
while True:
    t1.forward(random.randint(1,10))
    t2.forward(random.randint(2,9))
    t3.forward(random.randint(3,8))
    #比赛结束
    if t1.xcor() >= 200:
        t.write("幸运形是圆形！", align='center', font=('宋体', 30))
        break
    if t2.xcor() >= 200:
        t.write("幸运形是正方形！", align='center', font=('宋体', 30,))
        break
    if t3.xcor() >= 200:
        t.write("幸运形是三角形！", align='center', font=('宋体', 30,))
        break

#第六步：停止绘制，使窗口停留
t.done()

