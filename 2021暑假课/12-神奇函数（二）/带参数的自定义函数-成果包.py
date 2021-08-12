import turtle as t
t.speed(10)#增加画笔海龟绘制速度

def anyone(num):
    for x in range(num):
        t.fd(100)
        t.right(360/num)

#修改参数，查看绘制任意边数的图形

anyone(10)
t.done()







