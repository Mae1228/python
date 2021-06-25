'''随机幸运球v2.0'''
import random

flag = random.randint(1, 9)  # 随机生成1-9之间的一个数字
ball = []  # 存放幸运球

def lucky_ball():
    for i in range(1, 51):
        if i % flag == 0:
            ball.append(i)
    return ball

lucky_ball()
print('随机幸运球编号为'+str(flag)+'的倍数', ball)


