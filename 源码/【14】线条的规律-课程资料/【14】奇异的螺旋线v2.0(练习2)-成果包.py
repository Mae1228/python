'''海龟螺旋线v2.0'''
#调用turtle模块
import turtle as t
#画笔设置
t.pensize(1)
t.speed(10)
t.pencolor('blue')
#绘制螺旋线
for x in range(0, 401, 10):
    t.forward(x)
    #调整旋转角度
    t.right(73)
#隐藏画笔
t.hideturtle()
#阻止界面自动关闭(改为点击关闭)
t.done()



