''''''
'''
绘制指定半径的圆弧：t.circle(半径,弧度)   弧度：不写，默认是360度
半径：正：正左侧（半径为正圆心在左侧）     负：负右侧（半径为负圆心在右侧）
弧度：正：向海龟方向前进   负：向海龟方向后退（海龟方向不变）
设置填充颜色：t.fillcolor(颜色的字符串)  red blue white cyan
开始填充：t.begin_fill()   必须与t.end_fill()搭配使用
结束填充t.end_fill()    必须与t.begin_fill()搭配使用
填充三剑客：t.begin_fill()与t.end_fill()搭配使用      填充区域：起点和终点连线后所围成的封闭图形
随机库：random
随机产生整数：random.randint(小,大)   包头包尾
隐藏画笔：t.hideturtle()
'''
'''实践一：画圆：使用forward和left、right等方法实现'''
# import turtle as t
# t.speed(0)
# for i in range(360):
#     t.forward(1)
#     t.left(1)
# t.done()



'''实践二：画圆弧：正左侧：使用circle'''
# import turtle as t
# t.circle(100,270)
# t.done()



'''实践二：画圆弧：负右侧：使用circle'''
# import turtle as t
# t.circle(-100,270)
# t.done()



'''实践三'''
# import turtle as t
# t.circle(-100,180)
# t.done()



'''实践四：转弯'''
# import turtle as t
# t.right(180)
# t.circle(-100,90)
# t.done()



'''实践四：后退'''
# import turtle as t
# t.circle(100,-90)#方向水平向右
# t.done()



'''实践五：'''
# import turtle as t
# t.fillcolor('cyan')
# t.begin_fill()
# t.circle(-100,180)
# t.end_fill()
# t.hideturtle()
# t.done()



'''秘密星轨'''
# import turtle as t
# import random
# t.speed(10)
# t.fillcolor('black')
# t.begin_fill()
# t.penup()
# t.goto(-400,-400)
# t.pendown()
# for i in range(4):
#     t.forward(800)
#     t.left(90)
# t.end_fill()
# t.pencolor('cyan')
# for j in range(50):
#     t.penup()
#     t.goto(0,0)
#     r=random.randint(1,400)
#     t.forward(r)
#     t.left(90)
#     t.pendown()
#     t.circle(r,random.randint(1,360))
# t.hideturtle()
# t.done()

'''-------------------------------------------------------------------------------------'''
# ？：注释
# a：全选
# x：剪切
# c：复制
# v：粘贴

# import turtle as t
# import random
# t.speed(0)
# t.penup()
# t.goto(-400,-400)
# t.pendown()#落笔
# t.fillcolor('black')
# t.begin_fill()
# for i in range(4):
#     t.forward(800)
#     t.left(90)
# t.end_fill()
# t.pencolor('cyan')
# for i in range(100):
#     t.penup()
#     t.goto(0,0)
#     r=random.randint(1,400)#半径
#     h=random.randint(1,360)#弧长
#     t.forward(r)#半径10
#     t.left(90)
#     t.pendown()
#     t.circle(r,h)
# t.hideturtle()
# t.done()


'''---------------------------------------------------------------'''

















