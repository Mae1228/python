'''练习3成果包——思维达人'''

import random
import time

def luckynums(nlist):
    '''根据球员编号列表，生成幸运数字池：'''
    luckynums = []
    l = len(nlist)
    for i in range(l-1):
        for j in range(i+1, l):
            temp = nlist[i]+nlist[j]
            luckynums.append(temp)
    return luckynums

#此函数为工程包给出的函数
def luckycouple(nlist, target):
    '''根据球员编号列表和幸运数字找出中奖的两名幸运球员'''
    t1 = time.perf_counter()
    l = len(nlist)
    for i in range(l-1):
        for j in range(i+1, l):
            if nlist[i]+nlist[j] == target:
                t2 = time.perf_counter()
                print(t2-t1)
                return nlist[i], nlist[j]
#此函数为新函数
def luckycouple2(nlist, target):
    '''根据球员编号列表和幸运数字找出中奖的两名幸运球员'''
    t1 = time.perf_counter()
    l = len(nlist)
    for i in range(l-1):
        another = target - nlist[i]  # 幸运数减去当前球员编号获得另一个球员编号
        if another in nlist: # 若有此编号的球员即找到了幸运couple
            t2 = time.perf_counter()
            print(t2-t1)
            return nlist[i], another
                

#主控制
numlist = [ 7, 11, 2, 15,  21, 14]  
print('球员有：',numlist)
luckyList = luckynums(numlist)
print('幸运数字有：',luckyList)
lucky = random.choice(luckyList)
print('幸运数字为：', lucky)
print('方法一：两名幸运球员为：', luckycouple(numlist, lucky))
print('方法二：两名幸运球员为：', luckycouple2(numlist, lucky))






