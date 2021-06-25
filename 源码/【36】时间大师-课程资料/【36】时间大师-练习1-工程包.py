'''
程序计时器————工程包
《疯狂的兔子》两种实现方法已给出如下，请使用perf_counter()方法测试两种实现方法的速度，并给出比较结论。
（固定代表月份的参数number值为30）
'''
import time

# 迭代法
def rabbit1(number):
    m1 = 1
    m2 = 1
    if number == 1 or number == 2:
        return 1
    else:
        for x in range(3, number + 1):
            m1, m2 = m2, m1 + m2
        return m2

# 递归法
def rabbit2(number):
    if number == 1 or number == 2:
        return 1
    else:
        return rabbit2(number - 1) + rabbit2(number - 2)
