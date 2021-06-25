'''
日期转换器————工程包
请你合理使用mktime()和localtime()两个方法实现输入日期（年-月-日），
输出该日期是星期几和当年的第几天。
'''
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
