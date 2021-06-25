'''随机幸运球v3.0'''
import random

total = 0  # 统计幸运球个数
flag = random.randint(1, 9)  # 随机生成1-9之间的一个数字
ball = []  # 存放幸运球

def lucky_ball():
    global total
    for i in range(1, 51):
        if i % flag == 0:
            ball.append(i)
            total += 1
    return total, ball

lucky_ball()
print('幸运球个数为：',total,'\n编号为：',ball)


