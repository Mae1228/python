'''循环圣诞树-while循环'''
# while循环
number = int(input('输入数字:'))
i = 1
x = 1
while i <= number:
    print(' ' * (number - i) + '~' * (i * 2 - 1))
    i += 1
while x <= number // 2:
    print(' ' * (number - 2) + '^' * 3)
    x += 1




