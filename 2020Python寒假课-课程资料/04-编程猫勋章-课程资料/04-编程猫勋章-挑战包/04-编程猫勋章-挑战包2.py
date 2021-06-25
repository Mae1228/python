'''
编程猫勋章-挑战包2
修改程序使绘制的彩虹色居中显示。
stamp: 标记修改点, 本文共有2个标记
'''

#第一步:导入绘图工具箱和自定义工具箱
import turtle as t
import bcmpic as b

#第二步：使用自定义工具箱绘制勋章底稿
#stamp1:挑战1
t.penup()
t.goto(0, -160)
t.fillcolor('gray')
t.begin_fill()
t.circle(160)
t.end_fill()

b.codemao_head()
b.codemao_ears()
b.codemao_comb()
b.codemao_mask()
b.codemao_nose()
b.codemao_logo()

# #第三步：绘制编程猫勋章的眼睛和嘴巴
# 眼睛
t.penup()
t.goto(45, -12)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(26)
t.end_fill()

t.penup()
t.goto(45, -4)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(18)
t.end_fill()

t.penup()
t.goto(50, 20)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(6)
t.end_fill()

t.penup()
t.goto(-45, -12)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(26)
t.end_fill()

t.penup()
t.goto(-45, -4)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(18)
t.end_fill()

t.goto(-40, 20)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(6)
t.end_fill()

# 嘴巴
t.penup()
t.goto(-20, -60)
t.pendown()
t.right(90)
t.fillcolor('red')
t.begin_fill()
t.circle(20, 180)
t.end_fill()
t.setheading(180)
t.forward(40)
t.speed(1)
#stamp2:挑战2
t.penup()
t.goto(-35, -90)
t.setheading(0)
t.right(90)
t.fillcolor('red')
t.begin_fill()
t.forward(40)
t.left(120)
t.forward(80)
t.setheading(-90)
t.forward(40)
t.end_fill()
t.hideturtle()

t.done()

