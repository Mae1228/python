'''蒙提霍尔悖论-成果包'''

#调用random库
import random
#初始化门列表和被选列表
doors = [0,0,0]
s_doors = []
#第一步：将编程猫随机放到其中一扇门后
x = random.randint(0, 2)
doors[x] = 1
#第二步：询问选择者选哪扇门，并标记
print('【0】 【1】 【2】')
choice = int(input('请选择一扇门:'))
res = doors.pop(choice)
s_doors.append(res)
#第三步：在未被选的两扇门中，选择并打开有雷电猴的一扇门。
for i in range(2):
    if doors[i] == 0:
        move=doors.pop(i)
        s_doors.append(move)
        break
print( '房主把剩下两扇门中的一扇打开，发现里面是一只雷电猴!他说：“我帮你排除掉这扇门”')
#第四步：询问选择者要不要换门，如果换……否则……
msg = input('接着他又说：“你要不要换没打开的那扇门!?”（换/不换:y/n）')
if msg == 'y':
    res = doors[0]
#第五步：判断选择者是否选中编程猫，并显示游戏结果
if res == 1:
    print('你找到编程猫了！！！')
else:
    print('没有选到呢。。。')
