'''练习3成果包——Lucky寿星'''
'''
帮助阿短找出可以去参加的生日party列表。
生日信息已以字典形式给出，而阿短只有星期三和星期天有空。
有效利用for循环完成此任务。
'''
from datetime import date
partyDate = {
    '编程猫':  date(2020, 3, 9),
    '渝小帅':  date(2020, 4, 8),
    '温温':    date(2020, 5, 15),
    '欧阳涂涂':date(2020, 5, 21),
    '叶清秋':  date(2020, 6, 14),
    '高欢':    date(2020, 8, 8),
    '边磊':    date(2020, 9, 11),
    '丛子柒':  date(2020, 9, 20),
}
myList =[]
for k,v in partyDate.items():
    week = date.isoweekday(v)
    if week == 3 or week == 7:
        myList.append(k+str(v))
print('可以去参加的生日party有：' + ''.join(myList))



