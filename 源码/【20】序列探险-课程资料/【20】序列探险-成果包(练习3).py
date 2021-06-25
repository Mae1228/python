'''序列探险——练习3'''

# 遍历列表
mylist = ['阿短', '绿豆', 'codemao', '小可', '美美', '佩奇', '乔治',
          '小可', '大熊', '美美', '希希', '乔治', '阿瑶', '雪儿', '婷婷']
newlist = []
for x in mylist:
    if x not in newlist:
        newlist.append(x)
print(newlist)

# 集合转换
mylist = ['阿短', '绿豆', 'codemao', '小可', '美美', '佩奇', '乔治',
          '小可', '大熊', '美美', '希希', '乔治', '阿瑶', '雪儿', '婷婷']
newlist = list(set(mylist))
print(newlist)

