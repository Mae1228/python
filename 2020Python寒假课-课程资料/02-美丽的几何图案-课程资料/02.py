''''''
'''
字典：可变容器模型，可存储任意类型对象。
      键值对方式。键是唯一的，重复的会替换掉，值可以是任何数据类型。
      访问：通过索引的方式，字符串是通过下标取值，字典是通过键取值。
随机库：
画笔速度：t.spend(数值)------0到10  
                            数值大于10或小于0.5，速度=0
                            速度=0-------最快，没有动画效果
                            速度=10------快
                            速度=6--------正常
                            速度=3--------慢
                            速度=1--------最慢   
'''
'''美丽的几何图形'''
# import turtle as t
# import random
# color_pool={
#     1:'red',
#     2:'orange',
#     3:'yellow',
#     4:'green',
#     5:'cyan',
#     6:'blue',
#     7:'purple'
# }
# t.speed(0)
# t.pencolor(color_pool[random.randint(1, 7)])
# x=random.randint(0,360)
# for i in range(1000):
#     t.forward(i)
#     t.left(x)
# t.done()


'''美丽的几何图形：粗细'''
# import turtle as t
# import random
# color_pool={
#     1:'red',
#     2:'orange',
#     3:'yellow',
#     4:'green',
#     5:'cyan',
#     6:'blue',
#     7:'purple'
# }
# t.speed(0)
# t.pencolor(color_pool[random.randint(1, 7)])
# x=random.randint(0,360)
# c=random.randint(0,3)
# for i in range(1000):
#     t.pensize(c)
#     t.forward(i)
#     t.left(x)
# t.done()


'''美丽的几何图形：彩色'''
# import turtle as t
# import random
# color_pool={
#     1:'red',
#     2:'orange',
#     3:'yellow',
#     4:'green',
#     5:'cyan',
#     6:'blue',
#     7:'purple'
# }
# t.speed(0)
# x=random.randint(0,360)
# c=random.randint(0,3)
# for i in range(1000):
#     t.pencolor(color_pool[random.randint(1, 7)])
#     t.pensize(c)
#     t.forward(i)
#     t.left(x)
# t.done()


'''美丽的几何图形：左右旋转'''
# import turtle as t
# import random
# color_pool={
#     1:'red',
#     2:'orange',
#     3:'yellow',
#     4:'green',
#     5:'cyan',
#     6:'blue',
#     7:'purple'
# }
# t.speed(0)
# x=random.randint(0,360)
# c=random.randint(0,3)
# z=random.randint(0,1)
# if z:
#     for i in range(1000):
#         t.pencolor(color_pool[random.randint(1, 7)])
#         t.pensize(c)
#         t.forward(i)
#         t.left(x)
# else:
#     for i in range(1000):
#         t.pencolor(color_pool[random.randint(1, 7)])
#         t.pensize(c)
#         t.forward(i)
#         t.right(x)
# t.done()


# import turtle as t
# import random
# color_pool={
#     1:'red',
#     2:'orange',
#     3:'yellow',
#     4:'green',
#     5:'cyan',
#     6:'blue',
#     7:'purple'
# }
# t.speed(0)
# t.pencolor(color_pool[random.randint(1,7)])
# j=random.randint(0,360)
# for i in range(10,1000,3):
#     t.forward(i)
#     t.left(j)
# t.done()


# color_pool={
#     1:'red',
#     2:'orange',
#     3:'yellow',
#     4:'green',
#     5:'cyan',
#     6:'blue',
#     7:'purple'
# }


# color_pool=['red','blue','orange','green','yellow','cyan','purple']
# import turtle as t
# t.speed(0)
# t.colormode(255)
# t.pensize(10)
# list=[]
# for i in range(256):
#     t.color((255,i,0))
#     t.circle(100,360/255)
# t.done()


# color_pool=['red','blue','orange','green','yellow','cyan','purple']
# color_pool={
#     1:'red',
#     2:'orange',
#     3:'yellow',
#     4:'green',
#     5:'cyan',
#     6:'blue',
#     7:'purple'
# }








import turtle as t
import random
t.pencolor('blue')
y=random.randint(0,360)
a=random.randint(1,2)
if a==1:
    for i in range(10,1000,1):
        t.forward(i)
        t.left(y)
else:
    for i in range(10,1000,1):
        t.forward(i)
        t.right(y)
t.done()


import random
# color_pool={
#     1:'red',
#     2:'orange',
#     3:'yellow',
#     4:'green',
#     5:'cyan',
#     6:'blue',
#     7:'purple'
# }
# color_pool=['red','blue','orange','green','yellow','cyan','purple']
# print(color_pool[random.randint(0,6)])




# if a==1:
#     print('1111')
# else:
#     print('2222')




























