''''''
'''
背景颜色：t.bgcolor(颜色)--------默认是白色背景
填充三剑客：填充颜色：t.fillcolor(颜色)
            开始填充：t.begin_fill()
            结束填充：t.end_fill()
shape:一个有效的形状名字符串
      "arrow", "turtle", "circle", 
      "square", "triangle", "classic"
画笔隐藏：t.hideturtle()
用来获取圆形选手当前的x坐标：t.xcor()
窗口中打印文字：t.write(内容,align="左中右", font=("字体名称", 字体大小, "字体类型"))
画笔颜色和填充颜色：t.color(颜色)
'''
'''奔跑的幸运形'''
# import turtle as t
# import random
# t.title('奔跑的幸运形')
# t.bgcolor('pink')
# t.pencolor('red')
# t.penup()
# t.goto(200,0)
# t.pendown()
# t.left(90)
# t.forward(100)
# t.fillcolor('red')
# t.begin_fill()
# t.right(90)
# t.forward(50)
# t.goto(200,50)
# t.end_fill()
# t.hideturtle()
# t.penup()
# t1 = t.Pen()
# t1.color("green")
# t1.shape('circle')
# t2 = t.Pen()
# t2.color("blue")
# t2.shape('square')
# t3 = t.Pen()
# t3.color("purple")
# t3.shape('triangle')
# t1.penup()
# t2.penup()
# t3.penup()
# t1.goto(-300,100)
# t2.goto(-300,0)
# t3.goto(-300,-100)
# t.goto(0,200)
# while True:
#     t1.forward(random.randint(1,10))
#     t2.forward(random.randint(1,10))
#     t3.forward(random.randint(1,10))
#     if t1.xcor()>=200:
#         t.write('圆形胜利！',align='center', font=('宋体', 30, 'normal'))
#         break
#     if t2.xcor()>=200:
#         t.write('正方形胜利！',align='center', font=('宋体', 30, 'normal'))
#         break
#     if t3.xcor()>=200:
#         t.write('三角形胜利！',align='center', font=('宋体', 30, 'normal'))
#         break
# t.done()


'''奔跑的幸运形：海龟'''
# import turtle as t
# import random
# t.title('奔跑的幸运形')
# t.bgcolor('pink')
# t.pencolor('red')
# t.penup()
# t.goto(200,0)
# t.pendown()
# t.left(90)
# t.forward(100)
# t.fillcolor('red')
# t.begin_fill()
# t.right(90)
# t.forward(50)
# t.goto(200,50)
# t.end_fill()
# t.hideturtle()
# t.penup()
# t1 = t.Pen()
# t1.color("green")
# t1.shape('circle')
# t2 = t.Pen()
# t2.color("blue")
# t2.shape('square')
# t3 = t.Pen()
# t3.color("purple")
# t3.shape('triangle')
# t4 = t.Pen()
# t4.color("yellow")
# t4.shape('turtle')
# t1.penup()
# t2.penup()
# t3.penup()
# t4.penup()
# t1.goto(-300,100)
# t2.goto(-300,0)
# t3.goto(-300,-100)
# t4.goto(-300,-200)
# t.goto(0,200)
# while True:
#     t1.forward(random.randint(1,10))
#     t2.forward(random.randint(1,10))
#     t3.forward(random.randint(1,10))
#     t4.forward(random.randint(1,10))
#     if t1.xcor()>=200:
#         t.write('圆形胜利！',align='center', font=('arial', 30, 'normal'))
#         break
#     if t2.xcor()>=200:
#         t.write('正方形胜利！',align='center', font=('arial', 30, 'normal'))
#         break
#     if t3.xcor()>=200:
#         t.write('三角形胜利！',align='center', font=('arial', 30, 'normal'))
#         break
#     if t4.xcor()>=200:
#         t.write('海龟胜利！',align='center', font=('arial', 30, 'normal'))
#         break
# t.done()


'''奔跑的幸运形：起止线和跑道'''
# import turtle as t
# import random
# t.title('奔跑的幸运形')
# t.bgcolor('pink')
# t.pencolor('red')
# t.penup()
# t.goto(220,0)
# t.pendown()
# t.left(90)
# t.forward(100)
# t.fillcolor('red')
# t.begin_fill()
# t.right(90)
# t.forward(50)
# t.goto(220,50)
# t.end_fill()
# t.hideturtle()
# t.penup()
# t.goto(-280,150)
# t.pendown()
# t.goto(-280,-250)
# for i in range(150,-251,-100):
#     t.penup()
#     t.goto(-280,i)
#     t.pendown()
#     t.goto(200,i)
# t.penup()
# t.pencolor('blue')
# t.goto(200,150)
# t.pendown()
# t.goto(200,-250)
# t.penup()
# t1 = t.Pen()
# t1.color("green")
# t1.shape('circle')
# t2 = t.Pen()
# t2.color("blue")
# t2.shape('square')
# t3 = t.Pen()
# t3.color("purple")
# t3.shape('triangle')
# t4 = t.Pen()
# t4.color("yellow")
# t4.shape('turtle')
# t1.penup()
# t1.goto(-300,100)
# t2.penup()
# t2.goto(-300,0)
# t3.penup()
# t3.goto(-300,-100)
# t4.penup()
# t4.goto(-300,-200)
# t.goto(0,200)
# while True:
#     t1.forward(random.randint(1,10))
#     t2.forward(random.randint(1,10))
#     t3.forward(random.randint(1,10))
#     t4.forward(random.randint(1,10))
#     if t1.xcor()>=200:
#         t.write('圆形胜利！',align='center', font=('arial', 30, 'normal'))
#         break
#     elif t2.xcor()>=200:
#         t.write('正方形胜利！',align='center', font=('arial', 30, 'normal'))
#         break
#     elif t3.xcor()>=200:
#         t.write('三角形胜利！',align='center', font=('arial', 30, 'normal'))
#         break
#     elif t4.xcor()>=200:
#         t.write('海龟胜利！',align='center', font=('arial', 30, 'normal'))
#         break
# t.done()


'''奔跑的幸运形：变红变黑'''
# import turtle as t
# import random
# t.title('奔跑的幸运形')
# t.bgcolor('pink')
# t.pencolor('red')
# t.penup()
# t.goto(220,0)
# t.pendown()
# t.left(90)
# t.forward(100)
# t.fillcolor('red')
# t.begin_fill()
# t.right(90)
# t.forward(50)
# t.goto(220,50)
# t.end_fill()
# t.hideturtle()
# t.penup()
# t.goto(-280,150)
# t.pendown()
# t.goto(-280,-250)
# for i in range(150,-251,-100):
#     t.penup()
#     t.goto(-280,i)
#     t.pendown()
#     t.goto(200,i)
# t.penup()
# t.pencolor('blue')
# t.goto(200,150)
# t.pendown()
# t.goto(200,-250)
# t.penup()
# t1 = t.Pen()
# t1.color("green")
# t1.shape('circle')
# t2 = t.Pen()
# t2.color("blue")
# t2.shape('square')
# t3 = t.Pen()
# t3.color("purple")
# t3.shape('triangle')
# t4 = t.Pen()
# t4.color("yellow")
# t4.shape('turtle')
# t1.penup()
# t1.goto(-300,100)
# t2.penup()
# t2.goto(-300,0)
# t3.penup()
# t3.goto(-300,-100)
# t4.penup()
# t4.goto(-300,-200)
# t.goto(0,200)
# while True:
#     t1.forward(random.randint(1,10))
#     t2.forward(random.randint(1,10))
#     t3.forward(random.randint(1,10))
#     t4.forward(random.randint(1,10))
#     if t1.xcor()>=200:
#         t1.color('red')
#         t2.color('black')
#         t3.color('black')
#         t4.color('black')
#         t.write('圆形胜利！',align='center', font=('arial', 30, 'normal'))
#         break
#     elif t2.xcor()>=200:
#         t2.color('red')
#         t1.color('black')
#         t3.color('black')
#         t4.color('black')
#         t.write('正方形胜利！',align='center', font=('arial', 30, 'normal'))
#         break
#     elif t3.xcor()>=200:
#         t3.color('red')
#         t2.color('black')
#         t1.color('black')
#         t4.color('black')
#         t.write('三角形胜利！',align='center', font=('arial', 30, 'normal'))
#         break
#     elif t4.xcor()>=200:
#         t4.color('red')
#         t2.color('black')
#         t3.color('black')
#         t1.color('black')
#         t.write('海龟胜利！',align='center', font=('arial', 30, 'normal'))
#         break
# t.done()


'''-------------------------------------------------------------------------------------------------'''















