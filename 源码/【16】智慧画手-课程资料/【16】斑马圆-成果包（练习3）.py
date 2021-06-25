'''练习3成果包——斑马圆'''
'''
程序中有效使用for循环。
程序中有效使用分支结构。
'''

#调用模块
import turtle as t

#画笔设置
t.speed(100)

for x in range(100, 1, -10):
    t.penup()
    t.goto(0, -50)
    t.pendown()
    if x % 20 == 0:
        t.color('black')
    else:
        t.color('white')
    t.begin_fill()
    t.circle(x, 360)
    t.end_fill()

t.hideturtle()
t.done()


'''斑马圆'''
# import turtle as t
# t.speed(10)
# t.penup()
# t.goto(0,-200)
# t.pendown()
# r=200
# for i in range(10):
#     if i%2==0:
#         t.fillcolor('black')
#         t.begin_fill()
#         t.circle(r)
#         t.end_fill()
#     else:
#         t.fillcolor('white')
#         t.begin_fill()
#         t.circle(r)
#         t.end_fill()
#     r-=20
# t.hideturtle()
# t.done()