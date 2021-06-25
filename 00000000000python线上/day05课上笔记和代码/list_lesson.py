#__author:  Administrator
#date:  2016/8/22

#
# name0='wuchao'
# name1='jinxin'
# name2='xiaohu'
# name3='sanpang'
# name4='ligang'
#
# names='wuchao jinxing xiaohu sanpang ligang'

# a=['wuchao','jinxin','xiaohu','sanpang','ligang',['wuchao','jinxin']]

#增删改查
#查  切片 []
# print(a[1:])#取到最后
# print(a[1:-1])#取到倒数第二值
# print(a[1:-1:1])#从左到右一个一个去取
# print(a[1::2])#从左到右隔一个去取
# print(a[3::-1])
# b=a[3::-1]
# print(b)#['sanpang', 'xiaohu', 'jinxin', 'wuchao']
# print(a[-2::-1])
# print(a[1:-1:-2])

#添加 append insert

# a.append('xuepeng')  #默认插到最后一个位置
# print(a)
# a.insert(1,'xuepeng') #将数据插入到任意一个位置
# print(a)

#修改
#
# a[1]='haidilao'
# print(a)
# a[1:3]=['a','b']
# print(a)


#删除 remove pop del

# a.remove(a[0])
# print(a)
# b=a.pop(1)
# print(a)
# print(b)
#
# del a[0]
# print(a)
# del a
# print(a)
# a.remove(['wuchao','jinxin'])
# print(a)


#count:计算某元素出现次数
# t=['to', 'be', 'or', 'not', 'to', 'be'].count('to')
# print(t)

#extend
# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)
# print(b)

# index #  根据内容找位置

# a = ['wuchao', 'jinxin', 'xiaohu','ligang', 'sanpang', 'ligang', ['wuchao', 'jinxin']]
#
#
# first_lg_index = a.index("ligang")
# print("first_lg_index",first_lg_index)
# little_list = a[first_lg_index+1:]
#
# second_lg_index = little_list.index("ligang")
# print("second_lg_index",second_lg_index)
#
# second_lg_index_in_big_list = first_lg_index + second_lg_index +1
#
# print("second_lg_index_in_big_list",second_lg_index_in_big_list)
# print("second lg:",a[second_lg_index_in_big_list])

# reverse

# a = ['wuchao', 'jinxin', 'xiaohu','ligang', 'sanpang', 'ligang']
# a.reverse()
# print(a)

# x = [4, 6, 2, 1, 7, 9]
# x.sort(reverse=True)
# print(x)#[1, 2, 4, 6, 7, 9]


a = ['wuchao', 'jinxin', 'Xiaohu','Ligang', 'sanpang', 'ligang']
# a.sort()
# print(a)

print(a.count("haidilao ge"))
print(a.pop())
print(a)













