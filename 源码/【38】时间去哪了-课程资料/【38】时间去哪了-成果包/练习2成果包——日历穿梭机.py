'''练习2成果包——日历穿梭机'''
'''
使用calendar模块完成过去日历或未来日历的查询。
Input： 年份、起始月、结束月
Output：当年月份范围内的日历
'''
import calendar
y = int(input('input years:'))
m1 = int(input('start month:'))
m2 = int(input('end month:'))
if m1 == m2:
     print(calendar.month(y, m1))
else:
    for i in range(m1,m2+1):
        print(calendar.month(y, i + 1))
        print('*' * 20)

