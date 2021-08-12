import turtle
t=turtle.Pen()
#开始定义蛇的样子
lens=2#蛇身子长度为2
rad=70#蛇身体弯曲的半径
angle=80#蛇弯曲的角度
neckrad=15#蛇头弯曲的半径（高度）
#调整画笔，准备开始画图
t.pensize(30)#画笔尺寸
t.pencolor('green')
t.seth(-40)#前近的方向：0代表向东，90度向北，180度向西，270度向南，负值表示相反方向
#开始画蛇身体
for x in range(lens):
    t.circle(rad,angle)
    t.circle(-rad,angle)
t.circle(rad,angle/2)
t.forward(rad/2)#直线前近
t.circle(neckrad,180)
t.forward(rad/2)
#画蛇身体结束
turtle.done()





