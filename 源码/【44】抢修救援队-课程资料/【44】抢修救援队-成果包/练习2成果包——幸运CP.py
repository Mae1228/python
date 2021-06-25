'''练习2成果包——幸运CP'''

import random

def luckynums(nlist):
    '''根据球员编号列表，生成幸运数字池：'''
    luckynums = []
    l = len(nlist)
    for i in range(l-1):
        for j in range(i+1, l):
            temp = nlist[i]+nlist[j]
            luckynums.append(temp)
    return luckynums

def luckycouple(nlist, target):
    '''根据球员编号列表和幸运数字找出中奖的两名幸运球员'''
    l = len(nlist)
    for i in range(l-1):
        for j in range(i+1, l):
            if nlist[i]+nlist[j] == target:
                return nlist[i], nlist[j]            

#主控制
numlist = [ 7, 11, 2, 15,  21, 14]  
print('球员有：',numlist)
luckyList = luckynums(numlist)
print('幸运数字有：',luckyList)
lucky = random.choice(luckyList)
print('幸运数字为：', lucky)
print('两名幸运球员为：', luckycouple(numlist, lucky))

