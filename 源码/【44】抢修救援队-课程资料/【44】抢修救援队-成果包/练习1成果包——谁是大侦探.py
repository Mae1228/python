'''练习1成果包——谁是大侦探'''
# 抓了a,b,c,d四名犯罪嫌疑人，其中有一人是小偷，审讯中：
# a说我不是小偷；
# b说c是小偷；
# c说小偷肯定是d；
# d说c胡说！
# 其中有三个人说的是实话，一个人说的是假话。
# 请编程推断谁是小偷（穷举法和逻辑表达式）。

def thief_is():
    '找出小偷'
    for thief in ['a', 'b', 'c', 'd']:
        a = 'a' != thief
        b = thief == 'c'
        c = thief == 'd'
        d = thief != 'd'
        honest = a + b + c + d
        if honest == 3:
            print("thief is %s" % thief)
thief_is()

