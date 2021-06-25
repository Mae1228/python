# 调用random库
import random
# 实践一:用随机索引访问列表中的元素
mylist = [1, 45, 'a', 'fd', 3, 's']
# randint(a,b):随机的索引(下标)从0到mylist长度减一
x=random.randint(0,len(mylist)-1)
print(mylist[x])

# 实践二:随机生成一个怪兽
names = ['时空魔神', '海底猿人', '植物怪兽', '火山怪鸟', '刺客超兽']
where = ['猪圈', '厕所里', '房顶上', '办公室']
doing = ['引起大规模停电', '抄作业', '喜极而泣', '偷西瓜', '玩火自焚', '倒立狂奔']
n=random.randint(0,len(names)-1)
w=random.randint(0,len(where)-1)
d=random.randint(0,len(doing)-1)
print(names[n], '在', where[w], doing[d])

# 实践三:用索引访问嵌套列表中的元素
mylist = [['codemao', 5], ['列表', 2], 0]
# 输出520codemao
print(mylist[0][1],mylist[1][1],mylist[2],mylist[0][0])

# 实践四:用list.pop()方法移除列表中的元素
mylist = [['codemao', 5], ['列表', 2], 0]
# 输出list.pop()的返回值
mylist[0].pop()
mylist[0].pop()
mylist[1].pop(1)
mylist.pop()
# 输出移除520codemao后的mylist列表
print(mylist)
