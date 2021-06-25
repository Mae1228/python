import time
dic = {
    0: '星期一',
    1: '星期二',
    2: '星期三',
    3: '星期四',
    4: '星期五',
    5: '星期六',
    6: '星期日',
}
date = input('输入日期（例 2020-3-12）:').split('-')
year = int(date[0])
month = int(date[1])
day = int(date[2])
tup = (year, month, day,0,0,0,0,0,0)
str_time = time.mktime(tup)
struct_time = time.localtime(str_time)
w = struct_time[6]
j = struct_time[7]
print('当天是', dic[w], ',是当年的第', j, '天。')

