'''疯狂的兔子-挑战包'''

# 调用时间库
import time
# 迭代法自定义函数
def rabbit1(number):
    r1 = 1
    r2 = 1
    if number == 1 or number == 2:
        return 1
    else:
        for x in range(3, number + 1):
            r1, r2 = r2, r1 + r2
        return r2
# 递归法自定义函数
def rabbit2(number):
    if number == 1 or number == 2:
        return 1
    else:
        return rabbit2(number - 1) + rabbit2(number - 2)

# 记录起始时间赋值给t0
t0 = time.time()
print(rabbit1(20))
# 记录结束时间赋值给t1
t1 = time.time()
# 打印t1-t0，即耗时
print('迭代用时：', str(t1-t0))

t0 = time.time()
print(rabbit2(20))
t1 = time.time()
print('递归用时：', str(t1-t0))
