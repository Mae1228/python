'''海龟螺旋线v1.0'''
'''
1.笔刷颜色为“blue”
2.图案为螺旋等边三角形
3.每一次循环笔刷增大0.2
'''
'''海龟螺旋线v1.0'''
#调用turtle模块
import turtle as t
#画笔设置
i = 1
t.pensize(i)
t.speed(10)
t.pencolor('blue')
#绘制螺旋线
for x in range(0, 361, 15):
    #调整粗细
    i += 0.2
    t.pensize(i)
    t.forward(x)
    t.right(120)
#隐藏画笔
t.hideturtle()
#阻止界面自动关闭(改为点击关闭)
t.done()


