'''喵星秘密基地排查zero星密探'''
import random

members = [i for i in range(50)]
while True:
    try:
        num = int(input('请输入抽检成员数量：'))
        break
    except ValueError:
        print('输入值不是数字，请重新输入。')

def check_zero(num):
    li = []
    for n in range(num):
        m = random.randint(0, len(members)-1)
        m = members[m]
        if m not in li:
            li.append(m)
            members.remove(m)
    try:
        for i in li:
            j = 1/i
    except ZeroDivisionError:
        print('发现zero星密探闯入基地！')
    else:
        print('未发现可疑人员，基地一切正常！')
    finally:
        print('抽检成员详情为：', li)


check_zero(num)
