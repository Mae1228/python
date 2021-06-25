import pdb
import random

#数独题目数据列表：空字符串代表待填空的区域
l0 = [2, 8, 4, 6, 5, 7, 3, 9, 1]
l1 = [3, ' ', 7, 9, 2, 4, 5, 6, 8]
l2 = [5, 6, 9, 8, 1, 3, 2, 7, 4]
l3 = [8, 2, 5, 7, 4, 9, 1, 3, 6]
l4 = [6, 9, 3, 1, ' ', 2, 4, 5, 7]
l5 = [7, 4, 1, ' ', 6, 5, 8, 2, 9]
l6 = [9, 7, 8, 2, 3, 1, 6, 4, 5]
l7 = [4, 3, 6, 5, 7, ' ', 9, 1, 2]
l8 = [1, 5, 2, 4, 9, 6, 7, 8, 3]
numList = [l0, l1, l2, l3, l4, l5, l6, l7, l8]
#数独答案字典：待填空的位置及答案（位置的行和列均以0开始计数）
numAnswer = {(1, 1): 1, (4, 4): 8, (5, 3): 3, (7, 5): 8}

def showGame():
    '''显示界面：根据数独题目最新数据来显示游戏界面'''
    for k in range(9):
        for i in range(9):
            print('+-----', end='')
        print('+')
        for j in range(9):
            print('|'+'  '+str(numList[k][j])+'  ', end='')
        print('|')

def posCheck(r, c):
    '''位置检测（判断玩家输入的位置是否有效，位置错误或位置处已填写数据均为无效位置）'''
    if (r < 0 or r > 6) or (c < 0 or c > 6):
        print('位置错误，需重新选择目标格子！')
        return False
    else:
        if numList[r][c] == ' ':
            return True
        else:
            print('位置已有数据，需重新选择目标格子！')
            return False

def numListUpdate(r, c, n):
    '''答案检测（判断玩家在选定位置输入的答案为答案字典中的数据，如果答案正确则更新题目数据列表）'''
    if n == numAnswer[r, c]:
        return True
    else:
        print('答案错误，需重新选择目标格子！')
        return False


# 以下为游戏主控制
count = len(numAnswer)  # 获取答案字典的长度，即数独游戏待填空的数量(数量越多，数独难度越高)
showGame()  # 显示游戏界面
while True:
        print('目前游戏空白格子数：', count)
        print('-----------------------')
        pos = input('请选择目标位置（行和列均以0开始计数）：如：2，3\n')
        row = int(pos[0])   # 从输入的字符串中截取行数据
        col = int(pos[-1])  # 从输入的字符串中截取列数据
        if posCheck(row, col):  # 进行位置检测
            answer = int(input('请输入目标位置的答案：'))
            if numListUpdate(row, col, answer):  # 进行位置上的答案检测
                showGame()  # 显示最新游戏界面
                if count == 0:  # 若空白格子数为0，则退出循环，游戏成功
                    print('恭喜你，游戏成功！')
                    break




