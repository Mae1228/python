'''测试高手-练习包'''

#实践一：将两个相关列表合并为一个字典

a = ['c','s','n','q']
b = ['继续执行', '执行下一条', '执行下一条', '退出']
c = {}
print('------将两个相关列表合并为一个字典------')
for i in range(4):
    c[a[i]]=b[i]
    print(c)
print('------已完成两个列表合并为一个字典------')

#实践二：计算20以内的所有偶数（(不含能被5整除)）累加和。
i = 0
total = 1
while i < 20:
    i = i + 2
    total = total+i
    if i % 5 == 0:
      continue
print('20以内的所有偶数（(不含能被5整除)）累加和为:', total)

#实践三：
def story1():
    print('一个土豪，每次出门都担心家中被盗，想买只狼狗栓门前护院，但又不想花钱雇人喂狗。')
    print('苦思良久后终得一法：每次出门前把wifi修改成无密码，然后放心出门。')
    print('每次回来都能看到十几个人捧着手机蹲在自家门口，从此无忧。')
    return '故事1不错吧！'

def story2():
    print('一位大爷到菜市场买菜，挑了3个西红柿到秤盘，摊主秤了下：“一斤半3块7。”')
    print('大爷：“做汤不用那么多。”去掉了最大的西红柿。')
    print('摊主:“一斤二两，3块。”')
    print('正当身边人想提醒大爷注意秤时，大爷从容地掏出了七毛钱，拿起刚刚去掉的那个大的西红柿，潇洒地走开了。')
    return '故事2不错吧'

print('-------有这里有两个故事来听听看吧：------')
print('            ------1-------            ')
story1()
print('            ------2-------            ')
story2()
