''''''
'''根据输入的边出现对应的正多边形'''
import turtle as t
a=int(input('请输入正多边形的边长:'))
if a>=3:
    t.speed(10)
    jd=(a-2)*180/a
    for i in range(a):
        t.forward(50)
        t.left(180-jd)
    t.hideturtle()
    t.done()
else:
    print('请输入至少3条边')