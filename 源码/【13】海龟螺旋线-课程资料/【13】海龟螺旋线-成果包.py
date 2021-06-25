'''海龟螺旋线-成果包'''

#调用模块
import turtle as t
#画笔设置
t.pensize(2)
t.speed(10)
t.pencolor('blue')
#绘制螺旋线
#调整range()方法的步长
for x in range(0, 100, 2):
    t.forward(x) 
    t.right(20)
#隐藏画笔
t.hideturtle()
#阻止界面自动关闭(改为点击关闭)
t.done()
