'''练习4成果包——幸运"7"游戏"'''
'''
计算机从某个数开始进行幸运"7"游戏，输出这个数字到1000之间所有符合游戏规则的数字。

输入起始数字，输出范围内所有符合规则的数字，最后输出游戏结束。
如：
Input:
请输入一个数:990
Output:
991
992
993
995
996
998
999
1000
幸运"7"游戏结束！
'''
'''方法一：while True'''
# num = int(input('请输入一个数：'))
# while True:
#     if num == 1000:
#         break
#     num += 1
#     if num % 7 == 0 or "7" in str(num):
#         continue
#     print(num)
# print('幸运"7"游戏结束！')


'''方法二：while'''
num = int(input('请输入一个数：'))
while num<=1000:
    num += 1
    if num % 7 == 0 or "7" in str(num):
        continue
    print(num)
print('幸运"7"游戏结束！')




