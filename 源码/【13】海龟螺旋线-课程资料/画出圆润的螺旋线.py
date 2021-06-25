''''''
'''蓝色螺旋状曲线：使用for循环，circle'''
import turtle as t
t.speed(0)
t.pencolor('blue')
for i in range(5,300,8):
    t.circle(i,180)
t.hideturtle()
t.done()