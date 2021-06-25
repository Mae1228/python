#编程猫勋章-自定义工具箱bcmpic

#第一步:导入绘图工具箱
import turtle as t
p = t.Pen()
p.hideturtle()
p.speed(10)
#----请勿修改已经给出的代码
'''头的轮廓'''
def codemao_head():
    p.setheading(0)
    p.penup()
    p.goto(0, -100)
    p.pendown()
    p.fillcolor('floral white')
    p.begin_fill()
    p.circle(100)
    p.end_fill()
    p.penup()
    p.setheading(0)

'''整体面罩'''
def codemao_mask():
    '''右侧胡须面罩'''
    p.setheading(0)
    p.penup()
    p.goto(0, -15)
    p.right(20)
    p.pendown()
    p.fillcolor('red')
    p.begin_fill()
    p.circle(150, 45)
    p.goto(100, 0)
    p.end_fill()
    p.penup()
    '''左侧胡须面罩'''
    p.setheading(180)
    p.penup()
    p.goto(0, -15)
    p.left(20)
    p.pendown()
    p.fillcolor('red')
    p.begin_fill()
    p.circle(-150, 45)
    p.goto(-100, 0)
    p.end_fill()
    p.penup()
    '''上方面罩'''
    p.setheading(90)
    p.penup()
    p.goto(0, -15)
    p.fillcolor('red')
    p.begin_fill()
    p.goto(100, 0)
    p.pendown()
    p.circle(100, 180)
    p.penup()
    p.goto(0, -15)
    p.end_fill() 
    p.penup()
    p.setheading(0)


'''橘色小鼻头'''
def codemao_nose():  
    p.setheading(90)
    p.penup()
    p.goto(0, -28)
    p.right(60)
    p.pendown()
    p.fillcolor('orange')
    p.begin_fill()
    p.forward(16)
    p.left(90)
    p.circle(16, 120)
    p.left(90)
    p.forward(16)
    p.end_fill()
    p.penup()
    p.setheading(0)


'''一双小耳朵'''
def codemao_ears():  
    #右侧
    p.setheading(27)
    p.penup()
    p.goto(0, 0)
    p.forward(100)
    p.left(35)
    p.pendown()
    p.fillcolor('floral white')
    p.begin_fill()
    p.circle(80, 40)
    p.left(70)
    p.circle(80, 40)
    p.end_fill()
    #左侧
    p.setheading(180 - 27)
    p.penup()
    p.goto(0, 0)
    p.forward(100)
    p.right(35)
    p.pendown()
    p.fillcolor('floral white')
    p.begin_fill()
    p.circle(-80, 40)
    p.right(70)
    p.circle(-80, 40)
    p.end_fill()
    p.penup()
    p.setheading(0)


'''编程猫头饰logo'''
def codemao_logo(): 
    p.setheading(35)
    p.penup()
    p.goto(0, 30)
    p.pendown()
    p.fillcolor('orange')
    p.begin_fill()
    p.forward(55)
    p.left(110)
    p.forward(55)
    p.left(70)
    p.forward(55)
    p.left(110)
    p.forward(55)
    p.end_fill()
    p.penup()
    p.goto(-19, 36)
    p.write('编', font=("Arial", 31, 'bold'))
    p.setheading(0)


'''编程猫头冠'''
def codemao_comb():
    p.setheading(72)
    p.penup()
    p.goto(0, 0)
    p.forward(100)
    p.pendown()
    p.right(30)
    p.fillcolor('orange')
    p.begin_fill()
    p.circle(25, 150)
    p.circle(-100, 18)
    p.circle(-60, 20)
    p.circle(-20, 30)
    p.left(130)
    p.circle(35, 60)
    p.circle(20, 30)
    p.circle(-15, 70)
    p.end_fill()
    p.penup()
    p.setheading(0)
#----请勿修改已经给出的代码
