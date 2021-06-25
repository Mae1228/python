'''序列探险——练习1'''

# 切片操作列表，list()生成列表
a = '朝千两轻辞里岸舟白江猿已帝陵声过彩一蹄万云日不重间还住山，。，。'
b = ''
for i in range(4):
    b += a[i::4]
mylist = list(b)
print(mylist)

