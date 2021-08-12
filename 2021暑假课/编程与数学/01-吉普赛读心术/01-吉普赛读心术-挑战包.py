# 让玩家从10~79之间随便选一个数字，然后用这个数字加上十位上数字的三倍，
# 再减去个位上的数字得到一个新的数字。使用新数字在字母表（标号1到100）中找到对应的字母。
# 之后程序给出玩家刚刚找到的字母。
import random

dic = {}
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
m = s[random.randint(0, 25)]  # 随机选择一个字母作为正确答案
for i in range(1, 101):
    if i % 13 == 0:
        dic[i] = m
    else:
        n = random.randint(0, 25)
        dic[i] = s[n]

print(dic)
input('请从10~79之间任选一个数字，再用这个数依次加上十位上数字的三倍，减去个位上的数字得到一个新的数字然后把这个新数作为编号在上面找到对应的字母')

print('您刚才选中的字母是:', m)
