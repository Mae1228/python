''''''
'''
随机产生小数：random.uniform(小,大)
切换RGB色彩模式：t.colormode(mode)
                1、RGB小数模式：1.0
                2、RGB整数模式：255




'''
'''circle螺旋线'''
# import turtle as t
# t.speed(0)
# for i in range(200):
#     t.circle(i,30)
# t.hideturtle()
# t.done()



'''多彩繁星'''
# import turtle as t
# import random
# # t.speed(0)
# t.fillcolor('black')
# t.penup()
# t.goto(-300,-300)
# t.pendown()
# t.begin_fill()
# for i in range(4):
#     t.forward(600)
#     t.left(90)
# t.end_fill()
# for i in range(150):
#     t.pensize(random.randint(1,3))
#     t.pencolor(random.uniform(0.5,1),random.uniform(0.5,1),random.uniform(0.5,1))
#     t.penup()
#     x=random.randint(-300,300)
#     y=random.randint(-300,300)
#     t.goto(0,0)
#     t.goto(x,y)
#     t.pendown()
#     t.forward(1)
# t.hideturtle()
# t.done()


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


'''绘制爱心'''
# import turtle as t
# t.title('绘制爱心')
# t.penup()
# t.goto(0,-310)
# t.pendown()
# t.color('red','pink')
# t.begin_fill()
# t.left(45)
# t.forward(400)
# t.circle(200,180)
# t.right(90)
# t.circle(200,180)
# t.forward(400)
# t.hideturtle()
# t.end_fill()
# t.done()


'''------------------------------------------------------------------------------'''






import turtle as t
t.speed(10)
t.penup()
t.goto(0,-200)
t.pendown()
r=200
for i in range(1,11):
    if i%2==0:
        t.fillcolor('white')
    else:
        t.fillcolor('black')
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    r-=20
t.hideturtle()
t.done()






















