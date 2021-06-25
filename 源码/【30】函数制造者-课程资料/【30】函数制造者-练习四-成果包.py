'''函数制造者-练习四'''

# 定义取近似值函数
def myround(x, b=0):
    # 小数点向后移动b+1位
    y = int(x * 10 ** (b+1))
    rnd = y // 10
    # 取余
    f = y % 10
    if f > 4:
        rnd = rnd + 1
    # 小数点向前移动b位
    rnd *= 10 ** (-b)
    return rnd
    
# 输入小数和位数
msg = float(input('请输入要取近似值的浮点数：'))
mark = int(input('请输入要保留小数点后的位数：'))
# 调用四舍五入函数
res = myround(msg, mark)
print(msg,'取近似值后的结果是：',res)
