#北斗七星
import turtle
t=turtle.Pen()
turtle.bgcolor('black')
t.pencolor('yellow')
#移动初始位置到(-300，0)
t.penup()
t.goto(-300,0)
t.pendown()

#绘制第一颗星摇光
t.dot(20,'green')
t.write('摇光',font=('Arial',23,'bold'))
t.lt(30)#等效于t.left(50)
t.forward(5*20)

#绘制第二颗星开阳
t.dot(20,'blue')
t.write('开阳',font=('Arial',23,'bold'))
t.rt(50)#等效于t.right(50)
t.forward(5*20)

#绘制第三颗星玉衡
t.dot(20,'yellow')
t.write('玉衡',font=('Arial',23,'bold'))
t.lt(3)
t.forward(7*20)

#绘制第四颗星天权
t.dot(20,'red')
t.write('天权',font=('Arial',23,'bold'))
t.rt(55)#等效于t.right(50)
t.forward(6*20)

#绘制第五颗星天玑
t.dot(20,'white')
t.write('天玑',font=('Arial',23,'bold'))
t.lt(80)
t.forward(8*20)

#绘制第六颗星天璇
t.dot(20,'pink')
t.write('天璇',font=('Arial',23,'bold'))
t.lt(80)
t.forward(8*20)

#绘制第七颗星天枢
t.dot(20,'orange')
t.write('天枢',font=('Arial',23,'bold'))

turtle.done()









