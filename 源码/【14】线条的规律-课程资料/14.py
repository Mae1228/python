''''''
'''
画图库：turtle（海龟）
使用海龟库：import turtle as t
画笔：默认在（0,0）位置，默认是向右的方向，默认是落笔状态，默认是黑色
设置画笔粗细：turtle.pensize(粗细)
设置画笔颜色：turtle.pencolor(颜色)  默认是黑色
设置画笔前往方向：turtle.forward(长度)   默认是向右移动
设置画笔旋转：向左旋转：turtle.left(旋转角度)     向右旋转：turtle.right(旋转角度)
隐藏画笔：turtle.hideturtle()
阻止画板自动关闭：turtle.done()
n边形的内角和：（n-2）*180度
设置画笔速度：turtle.speed(0到10)   0：最快   10：快   6：正常   3：慢   1：最慢   
画笔前往定位方向：turtle.goto(x,y)   默认在（0,0）位置
落笔：turtle.pendown()   默认是落笔状态
抬笔：turtle.penup()
'''
'''三角形'''
# import turtle as t
# i=1
# t.pencolor('blue')
# for j in range(1,200,8):
#     i+=0.2
#     t.pensize(i)
#     t.forward(j)
#     t.right(120)
# t.hideturtle()
# t.done()

'''五边形'''
# import turtle as t
# t.pencolor('blue')
# for j in range(1,200,4):
#     t.forward(j)
#     t.right(73)
# t.hideturtle()
# t.done()

'''棋盘：向右横，向下竖'''
# import turtle as t
# for h in range(0,-181,-10):
#     t.goto(0,h)
#     t.pendown()
#     t.goto(180,h)
#     t.penup()
# for s in range(0,181,10):
#     t.goto(s,0)
#     t.pendown()
#     t.goto(s,-180)
#     t.penup()
# t.hideturtle()
# t.done()


'''居中画棋盘'''
# import turtle as t
# t.speed(10)
# t.pencolor('red')
# t.fillcolor('red')
# t.begin_fill()
# t.circle(2)
# t.end_fill()
# t.pencolor('black')
# for x in range(-90,91,10):
#     t.penup()
#     t.goto(x,90)
#     t.pendown()
#     t.goto(x,-90)
# for y in range(90,-91,-10):
#     t.penup()
#     t.goto(90,y)
#     t.pendown()
#     t.goto(-90,y)
# t.hideturtle()
# t.done()

'''横竖画棋盘'''
# import turtle as t
# t.speed(10)
# for x in range(0,181,10):
#     t.goto(x,0)
#     t.pendown()
#     t.goto(x,-180)
#     t.penup()
#     t.goto(0,-x)
#     t.pendown()
#     t.goto(180,-x)
#     t.penup()
# t.hideturtle()
# t.done()


'''-----------------------------------------------------------------------------------------------'''



















