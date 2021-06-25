''''''
'''
绘图库：turtle（海龟）
使用绘图库：import turtle     写在第一行
使用绘图库（起小名）：import turtle as t     写在第一行
前进画线：t.forward(距离)   t：库名   .：调用、使用    forward():前进方法
转弯：向左转：t.left(旋转角度)        向右转弯：t.right(旋转角度)
画笔起点：默认位置：（0,0）   默认方向：水平向右
防止画板自动关闭：t.done()    写在最后一行
隐藏画笔：t.hideturtle()
画笔速度：t.speed(1到10)  1到10：逐渐变快   0：最快
画笔粗细：t.pensize(大小)
画笔颜色：t.pencolor(颜色等字符串)     白色:white   黑色:black   灰色:grey   粉色:pink
            红色:red   橙色:orange   黄色:yellow   绿色:green   蓝色:blue   紫色:purple

for循环：计算机做有规律的事件用到循环
range(start,stop,step)：start：默认从0开始     stop：结束不包括stop本身    step：步长，默认为1
'''
'''横折横 '''
# import turtle as t
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.hideturtle()
# t.done()



'''正方形：无颜色无粗细'''
# import turtle as t
# t.forward(50)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.hideturtle()
# t.done()


'''正方形：颜色和粗细'''
# import turtle as t
# t.pensize(2)
# t.pencolor('red')
# t.forward(50)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.hideturtle()
# t.done()


'''正方形：使用for循环简化代码量'''
# import turtle as t
# t.pensize(2)
# t.pencolor('red')
# for i in range(4):
#     t.forward(50)
#     t.right(90)
# t.hideturtle()
# t.done()


'''蓝色螺旋状曲线：使用for循环，right'''
# import turtle as t
# t.pencolor('blue')
# t.speed(10)
# for i in range(1,100,2):
#     t.forward(i)
#     t.right(20)
# t.hideturtle()
# t.done()


'''挑战：红色和蓝色螺旋状曲线'''
# import turtle as t
# t.speed(10)
# t.pensize(5)
# t.pencolor('blue')
# for i in range(1,100,2):
#     t.forward(i)
#     t.right(20)
# t.pencolor('red')
# for i in range(100,1,-2):
#     t.forward(i)
#     t.right(20)
# t.hideturtle()
# t.done()


'''蓝色螺旋状曲线：使用for循环，circle'''
# import turtle as t
# t.speed(0)
# t.pencolor('blue')
# for i in range(5,300,8):
#     t.circle(i,180)
# t.hideturtle()
# t.done()


# '''根据输入的边出现对应的正多边形'''
# import turtle as t
# a=int(input('请输入正多边形的边长:'))
# if a>=3:
#     t.speed(10)
#     jd=(a-2)*180/a
#     for i in range(a):
#         t.forward(50)
#         t.left(180-jd)
#     t.hideturtle()
#     t.done()
# else:
#     print('请输入至少3条边')


































