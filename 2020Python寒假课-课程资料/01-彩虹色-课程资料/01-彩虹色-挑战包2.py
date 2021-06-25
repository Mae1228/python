'''
彩虹色-挑战包2
利用所学内容绘制斑马线。
'''

#第一步：导入绘图工具箱
import turtle as t

#第二步：绘制第一条白色线
t.pencolor("white")
t.pensize(30)
t.penup()
t.goto(-150, -200)
t.pendown()
t.forward(300)

#第二步：绘制黑色线
t.pencolor("black")
t.penup()
t.goto(-150, -200+30)
t.pendown()
t.forward(300)

#第五步：绘制完整斑马线
t.pencolor("white")
t.penup()
t.goto(-150, -200+60)
t.pendown()
t.forward(300)

t.pencolor("black")
t.penup()
t.goto(-150, -200+90)
t.pendown()
t.forward(300)

t.pencolor("white")
t.penup()
t.goto(-150, -200+120)
t.pendown()
t.forward(300)

t.pencolor("black")
t.penup()
t.goto(-150, -200+150)
t.pendown()
t.forward(300)

t.pencolor("white")
t.penup()
t.goto(-150, -200+180)
t.pendown()
t.forward(300)

t.pencolor("black")
t.penup()
t.goto(-150, -200+210)
t.pendown()
t.forward(300)

t.pencolor("white")
t.penup()
t.goto(-150, -200+240)
t.pendown()
t.forward(300)

t.pencolor("black")
t.penup()
t.goto(-150, -200+270)
t.pendown()
t.forward(300)

t.pencolor("white")
t.penup()
t.goto(-150, -200+300)
t.pendown()
t.forward(300)

t.pencolor("black")
t.penup()
t.goto(-150, -200+330)
t.pendown()
t.forward(300)

t.pencolor("white")
t.penup()
t.goto(-150, -200+360)
t.pendown()
t.forward(300)

t.pencolor("black")
t.penup()
t.goto(-150, -200+390)
t.pendown()
t.forward(300)

t.done()








