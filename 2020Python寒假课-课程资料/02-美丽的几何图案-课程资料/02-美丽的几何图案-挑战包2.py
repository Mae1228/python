'''
美丽的几何图案-挑战包2
修改随机颜色的设置，使每一条线的颜色都不同
'''

#色彩池，在其中添加自己喜欢的颜色
# color_pool = {
#     1: 'red',
#     2: 'blue',
#     3: 'orange',
#     4: 'green',
#     #使用与上方完全相同的格式，继续添加新颜色
#     5: 'yellow',
#     6: 'cyan',
#     7: 'purple',
# }
color_pool=['red','blue','orange','green','yellow','cyan','purple']
import turtle as t
import random
t.speed(10)
x = 10
y = random.randint(0, 360)
t.pensize(random.randint(1, 3))
for i in range(1000):
    c = color_pool[random.randint(0, 6)]
    t.pencolor(c)
    t.forward(x)
    t.left(y)
    x += 1
t.done()
