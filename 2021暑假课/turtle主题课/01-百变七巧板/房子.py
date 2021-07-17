# 百变七巧板
import turtle as t
t.setup(800, 500)
t.bgpic('背景图.png')

#②以下七块拼成了一个完整的房子，加载02背景图的任务就是补充其中的第一块和第四块。
# 第一块
p = t.Pen()
p.color('red')
p.penup()
p.goto(0, 0)
p.pendown()
p.begin_fill()
p.goto(-100, -100)
p.goto(100, -100)
p.end_fill()
# 第二块
p.color('orange')
p.penup()
p.goto(0, 0)
p.pendown()
p.begin_fill()
p.goto(-100, 0)
p.goto(-100, -100)
p.end_fill()
# 第三块
p.color('yellow')
p.penup()
p.goto(100, 0)
p.pendown()
p.begin_fill()
p.goto(100, -100)
p.goto(50, -50)
p.end_fill()
# 第四块
p.color('green')
p.penup()
p.goto(100, 0)
p.pendown()
p.begin_fill()
p.goto(0, 0)
p.goto(50, -50)
p.end_fill()
# 第五块
p.color('cyan')
p.penup()
p.goto(50, 0)
p.pendown()
p.begin_fill()
p.goto(-150, 0)
p.goto(-50, 100)
p.end_fill()
# 第六块
p.color('blue')
p.penup()
p.goto(50, 0)
p.pendown()
p.begin_fill()
p.goto(50+1.414 * 50, 0)
p.goto(50, 1.414 * 50)
p.goto(50-1.414 * 50, 1.414 * 50)
p.end_fill()
# 第七块
p.color('purple')
p.penup()
p.goto(50, 1.414 * 50)
p.pendown()
p.begin_fill()
p.goto(50-1.414 * 50, 1.414 * 50)
p.goto(50-1.414 * 50, 1.414 * 50*2)
p.goto(50, 1.414 * 50*2)
p.end_fill()

p.hideturtle()
t.done()