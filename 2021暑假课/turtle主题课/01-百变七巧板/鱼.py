# 百变七巧板
import turtle as t
t.setup(800, 500)
t.bgpic('背景图.png')

# ③以下七块拼成了一个完整的鱼，加载03背景图的任务就是补充其中的第一块和第五块。
# 第一块
p = t.Pen()
p.color('red')
p.penup()
p.goto(0, 0)
p.pendown()
p.begin_fill()
p.goto(-2.828 * 50, 0)
p.goto(0, 2.828 * 50)
p.end_fill()
# 第二块
p.color('orange')
p.penup()
p.goto(0, 0)
p.pendown()
p.begin_fill()
p.goto(-2.828 * 50, 0)
p.goto(0, -2.828 * 50)
p.end_fill()
# 第三块
p.color('yellow')
p.penup()
p.goto(0, 0)
p.pendown()
p.begin_fill()
p.goto(0, 0.707 * 50)
p.goto(1.414 * 50, 0.707 * 50)
p.goto(1.414 * 50, -0.707 * 50)
p.goto(0, -0.707 * 50)
p.end_fill()
# 第四块
p.color('green')
p.penup()
p.goto(0, -2.121 * 50)
p.pendown()
p.begin_fill()
p.goto(0, -0.707 * 50)
p.goto(1.414 * 50, -0.707 * 50)
p.end_fill()
# 第五块
p.color('cyan')
p.penup()
p.goto(0, 2.121 * 50)
p.pendown()
p.begin_fill()
p.goto(0, 0.707 * 50)
p.goto(1.414 * 50, 0.707 * 50)
p.end_fill()
# 第六块
p.color('blue')
p.penup()
p.goto(1.414 * 50, 0.707 * 50)
p.pendown()
p.begin_fill()
p.goto(2.828 * 50, 2.121 * 50)
p.goto(2.828 * 50, -0.707 * 50)
p.end_fill()
# 第七块
p.color('purple')
p.penup()
p.goto(2.828 * 50, -0.707 * 50)
p.pendown()
p.begin_fill()
p.goto(1.414 * 50, 0.707 * 50)
p.goto(1.414 * 50, -0.707 * 50)
p.goto(2.828 * 50, -2.121 * 50)
p.end_fill()

p.hideturtle()
t.done()