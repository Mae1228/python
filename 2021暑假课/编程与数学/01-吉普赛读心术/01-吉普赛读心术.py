# 读心术 玩家从10~99任选一个数字，再用这个数
# 依次减去它的十位和个位上的数得到一个新的数字，
# 然后把这个新数作为编号在一个图表中找到对应的图形。

import random

dic = {}
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
m = s[random.randint(0, 25)]  # 随机选择一个字母作为正确答案
for i in range(1, 100):
    if i % 9 == 0:
        dic[i] = m
    else:
        n = random.randint(0, 25)
        dic[i] = s[n]

print(dic)
input('请从10~99之间任选一个数字，再用这个数依次减去它的十位和个位上的数得到一个新的数字，然后把这个新数作为编号在上面找到对应的字母')

print('您刚才选中的字母是:', m)
