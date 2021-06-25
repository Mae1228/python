'''神秘逻辑-练习一'''

#递归求解5的阶乘
def myfac(n):
    if n == 1:
        return 1
    else:
        return n * myfac(n - 1)

num = int(input('请输入数字：'))
print(myfac(num))