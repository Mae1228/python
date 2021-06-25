'''疯狂的兔子-练习包'''

# 迭代法求和函数
def mysum1(number):
    # 结果变量
    res = 0
    # 计数器
    i = 1
    while i <= number:
        res += i
        # 计数器每次循环增加1
        i += 1
    return res
    
# 递归法求和函数
def mysum2(number):
    # 递推判断条件
    if number == 1:
        return 1
    else: 
        # 返回number加（number-1）到1之间整数和
        return number + mysum2(number-1)

print(mysum1(100))
print(mysum2(100))