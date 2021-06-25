'''彩虹色-成果包'''

#第一步：导入绘图工具箱
import turtle as t

#第二步：绘制第一条彩虹色
t.pencolor("red")
t.pensize(30)
t.forward(300)

#第三步：绘制第二条彩虹色
t.pencolor("orange")
t.penup()
t.goto(0, 30)
t.pendown()
t.forward(300)

#第四步：绘制完整彩虹色
t.pencolor("yellow")
t.penup()
t.goto(0, 60)
t.pendown()
t.forward(300)

t.pencolor("green")
t.penup()
t.goto(0, 90)
t.pendown()
t.forward(300)

t.pencolor("cyan")
t.penup()
t.goto(0, 120)
t.pendown()
t.forward(300)

t.pencolor("blue")
t.penup()
t.goto(0, 150)
t.pendown()
t.forward(300)

t.pencolor("purple")
t.penup()
t.goto(0, 180)
t.pendown()
t.forward(300)

t.done()








