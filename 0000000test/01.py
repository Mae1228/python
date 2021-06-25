import turtle as t
t.setup(500, 400, 200, 200)
t.penup()
t.fd(-250)
t.pendown()
t.pensize(20)
t.seth(-40)
r = 0.1
g = 0.2
b = 0.3
for i in range(4):
    t.pencolor((r+0.1*i, g+0.1*i, b+0.1*i))
    t.circle(40, 80)
    t.circle(-40, 80)
    t.pencolor((r+0.1*4, g+0.1*4, b+0.1*4))
    t.circle(40, 80/2)
    t.fd(40)
    t.pencolor((r+0.1*5, g+0.1*5, b+0.1*5))
    t.circle(16, 180)
    t.fd(40*2/3)

t.done()