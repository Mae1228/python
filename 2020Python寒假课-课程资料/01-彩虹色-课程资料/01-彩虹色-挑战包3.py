'''
彩虹色-挑战包3
一笔绘制彩虹色。
'''

#第一步：导入绘图工具箱
import turtle as t

#第二步：绘制第一条彩虹色
t.pencolor("red")
t.pensize(30)
t.penup()
t.goto(-150, 0)
t.pendown()
t.forward(300)

#第三步：绘制第二条彩虹色
t.goto(150, 30)
t.pencolor("orange")
t.left(180)
t.forward(300)

#第四步：绘制完整彩虹色
t.goto(-150, 60)
t.pencolor("yellow")
t.right(180)
t.forward(300)

t.goto(150, 90)
t.pencolor("green")
t.left(180)
t.forward(300)

t.goto(-150, 120)
t.pencolor("cyan")
t.right(180)
t.forward(300)

t.goto(150, 150)
t.pencolor("blue")
t.left(180)
t.forward(300)

t.goto(-150, 180)
t.pencolor("purple")
t.right(180)
t.forward(300)

t.done()








