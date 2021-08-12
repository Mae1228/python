#定义无参数有返回值函数
def fun3():
    print('我是fun3，我没有参数，但是有返回值')
    print('今日温度获取中......')
    #假设已经获取到今日气温是18摄氏度
    code=18
    print('返回值：',code)
    #使用return 返回查询到的数据
    return code

number=fun3()
print('今日气温是：{}摄氏度'.format(number))











