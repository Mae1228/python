'''海龟螺旋线-挑战包'''

#调用模块
import turtle as t
t.pensize(4)
t.pencolor("blue")
t.speed(10)
#绘制螺旋线
#调整range()方法的步长
for x in range(0, 100, 2):
    t.forward(x)
    t.right(20) 
#改变画笔颜色为红色
t.pencolor("red")
#绘制反向螺旋线
for x in range(100,0,-2):
    t.forward(x)
    t.right(20) 
#隐藏画笔
t.hideturtle()
#阻止界面自动关闭(改为点击关闭)
t.done()



