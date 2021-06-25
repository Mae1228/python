'''随机怪兽生成器-挑战包'''
# 调用random库
import random
# 随机池
mylist = [['时空魔神', '海底猿人', '植物怪兽', '火山怪鸟', '刺客超兽'], 
       ['猪圈', '厕所里', '房顶上', '办公室'], 
       ['引起大规模停电', '抄作业',  '偷西瓜', '玩火自焚', '倒立狂奔'],
       ['触发被动技能【挨揍】', '触发被动技能【犯傻】','续命0.001秒']]
# 定义一个空列表
temp=[[],[],[],[]]
# 死循环:不断随机生成新怪兽
while 1:
    # 四个子表都不为空
    if mylist[0] and mylist[1] and mylist[2] and mylist[3]:
        #按下Enter键生成怪兽
        if input('***Press Enter***见证怪兽的时刻到了：') == '':
            #获取索引：从0到mylist[0]长度减1之间随机获取一个整数
            n = random.randint(0, (len(mylist[0]) - 1))
            w = random.randint(0, (len(mylist[1]) - 1))
            d = random.randint(0, (len(mylist[2]) - 1))
            b = random.randint(0, (len(mylist[3]) - 1))
            print(mylist[0][n], '在', mylist[1][w], mylist[2][d],mylist[3][b])
            #x用来接收子列表mylist[0]移除(pop)的元素mylist[0][n]
            x = mylist[0].pop(n)
            #temp[0]子列表加入新元素x
            temp[0].append(x)
            x = mylist[1].pop(w)
            temp[1].append(x)
            x = mylist[2].pop(d)
            temp[2].append(x)
            x = mylist[3].pop(b)
            temp[3].append(x)
        #键入其他值结束死循环
        else:
            break
    else: #如果四个子表有一个为空
        if len(mylist[0]) == 0:
            temp[0], mylist[0] = mylist[0], temp[0]
        if len(mylist[1]) == 0:
            temp[1], mylist[1] = mylist[1], temp[1]
        if len(mylist[2]) == 0:
            temp[2], mylist[2] = mylist[2], temp[2]
        if len(mylist[3]) == 0:
            temp[3], mylist[3] = mylist[3], temp[3]
