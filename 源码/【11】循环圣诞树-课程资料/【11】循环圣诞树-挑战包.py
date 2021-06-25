'''循环圣诞树-挑战包'''
'''stamp:标记修改点,本文共有3个标记'''

number = int(input('输入数字:'))
# stamp1:增加计数器,用于计算每行填充字符的个数，实现分层效果
i = 1
for x in range(1, number + 1):
    # stamp2:修改变量
    print((' ' * (number - i) + '~' * (i * 2 - 1)))
    # stamp3:判断，每五层一个阶梯
    if (x % 5 == 0):
        i -= 2
    else:
        i += 1
for x in range(1, number // 2 + 1):
    print((' ' * (number - 2) + '^' * 3))
