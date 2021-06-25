'''循环圣诞树-for循环'''

# for循环
while True:
    number = int(input('输入数字:'))
    for i in range(1, number + 1):
        print(' ' * (number - i) + '~' * (i * 2 - 1))
    for x in range(1, number // 2 + 1):
        print(' ' * (number - 2) + '^' * 3)
