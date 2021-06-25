'''疯狂的兔子-成果包'''

# 迭代法自定义函数
def rabbit1(number):
    m1 = 1
    m2 = 1
    if number == 1 or number == 2:
        return 1
    else:
        for x in range(3, number + 1):
            # 多元赋值
            m1, m2 = m2, m1 + m2
        return m2
# 递归法自定义函数
def rabbit2(number):
    if number == 1 or number == 2:
        return 1
    else:
        return rabbit2(number - 1) + rabbit2(number - 2)

print(rabbit1(12))
print(rabbit2(12))
