'''练习1成果包——circle螺旋线'''
'''
程序中有效使用for循环。
'''

#调用模块
import turtle as t

#画笔设置
t.speed(100)

for r in range(150):
    t.circle(r, 30)

t.hideturtle()
t.done()

