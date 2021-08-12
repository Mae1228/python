#使用前声明全局变量
global name
#声明全局变量时不可赋值，需要另起一行赋值
name='默认的'
#定义有参数无返回值的自定义函数
def fun2(word):
    print('我是fun2，我有参数，但是没有返回值')
    global name#再次声明，表示这里的name时全局变量，不是函数内部局部变量
    name=word

print('name变量修改前内容：'+name)
#调用该函数
fun2('编程猫')
print('name变量修改之后的内容：'+name)














