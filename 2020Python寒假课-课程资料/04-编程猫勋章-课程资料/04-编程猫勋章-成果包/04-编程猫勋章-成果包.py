'''编程猫勋章-成果包'''

#第一步:导入绘图工具箱和自定义工具箱
import turtle as t
import bcmpic as b

t.title('编程猫勋章')

#第二步：使用自定义工具箱绘制勋章底稿

b.codemao_head()
b.codemao_ears()
b.codemao_comb()
b.codemao_mask()
b.codemao_nose()
b.codemao_logo()

#第三步：绘制编程猫勋章的眼睛和嘴巴
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
#左眼
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
t.hideturtle()

t.done()

