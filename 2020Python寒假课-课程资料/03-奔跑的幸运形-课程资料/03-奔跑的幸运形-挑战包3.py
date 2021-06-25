'''
奔跑的幸运形-挑战包3
胜利者为变为红色，其他图形变为黑色
'''

#第一步：导入海龟绘图工具箱和随机数工具箱
import turtle as t
import random 

#第二步：命名绘制窗口，设置背景色
t.title("奔跑的幸运形")
t.bgcolor("pink")

#第三步：绘制起跑线
t.color("red")
t.fillcolor("red")
t.penup()
t.goto(-280,150)
t.pendown()
t.goto(-280,-250)

#第四步：绘制跑道
temp=0
for i in range(5):
    t.penup()
    t.goto(-280, 150-temp)
    t.pendown()
    t.forward(480)
    temp+=100

#第五步：绘制终点线
t.color("blue")
t.fillcolor("blue")
t.penup()
t.goto(200, 150)
t.pendown()
t.goto(200, -250)
t.penup()
t.goto(0,200)
t.hideturtle()

#第六步：添加比赛的图形
t1 = t.Pen()
t1.color("green")
t1.shape('circle')
t2 = t.Pen()
t2.color("blue")
t2.shape('square')
t3 = t.Pen()
t3.color("purple")
t3.shape('triangle')
t4 = t.Pen()
t4.color("yellow")
t4.shape('turtle')
t1.penup()
t1.goto(-300, 100)
t2.penup()
t2.goto(-300, 0)
t3.penup()
t3.goto(-300, -100)
t4.penup()
t4.goto(-300, -200)

#第七步：开始赛跑
while True:
    t1.forward(random.randint(3, 8))
    t2.forward(random.randint(2, 9))
    t3.forward(random.randint(1, 10))
    t4.forward(random.randint(5, 6))
    if t1.xcor() >= 200:
        t.write("幸运形是圆形！", align='center', font=('arial', 30, 'normal'))
        t1.color('red')
        t2.color('black')
        t3.color('black')
        t4.color('black')
        break
    if t2.xcor() >= 200:
        t.write("幸运形是正方形！", align='center', font=('arial', 30, 'normal'))
        t1.color('black')
        t2.color('red')
        t3.color('black')
        t4.color('black')
        break
    if t3.xcor() >= 200:
        t.write("幸运形是三角形！", align='center', font=('arial', 30, 'normal'))
        t1.color('black')
        t2.color('black')
        t3.color('red')
        t4.color('black')
        break
    if t4.xcor() >= 200:
        t.write("幸运形是小海龟！", align='center', font=('arial', 30, 'normal'))
        t1.color('black')
        t2.color('black')
        t3.color('black')
        t4.color('red')
        break

#第八步：停止绘制，使窗口停留
t.done()

