'''杨辉三角完形挑战'''
#杨辉三角单行生成
#前三行
# list0 = [1]
# list1 = [1, 1]
# list2 = [1, 2, 1]
#第四行
list3 = [1, 3, 3, 1]
#第五行
list4 = []
#根据第四行，生成第五行
for x in range(len(list3)):
    #每行第一个元素是1，直接加到空列表里
    if x == 0:
        list4.append(1)
    #从每行第二个元素开始，按规律进行计算
    else:
        list4.append(list3[x] + list3[x - 1])
#每行最后一个元素是1，直接加到列表末尾
list4.append(1)
#打印第五行
print(list4)
