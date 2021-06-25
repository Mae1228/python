'''数字大小写转换器-成果包'''

#设置数字(number)转换字典
m = {
    '0': '零',
    '1': '壹',
    '2': '贰',
    '3': '叁',
    '4': '肆',
    '5': '伍',
    '6': '陆',
    '7': '柒',
    '8': '捌',
    '9': '玖',
}

#设置单位(unit)转换字典
u = {
    0: '元',
    1: '拾',
    2: '佰',
    3: '仟',
    4: '万',
}

#输入要转换的整数金额
message = input('输入数字:') 
#将字符串金额转为数字字符列表
message = list(message)

#用列表保存每个数字字符所对应的大写字符
mlist = []
#遍历数字字符列表
for x in message:
    #将每个数字字符所对应的大写字符添加到大写列表中
    mlist.append(m[x])

#用列表保存每位数字所对应的单位字符
ulist = []
#循环数字字符列表长度次
for x in range(len(message)):
    #将每位所对应的单位字符添加到单位列表中
    ulist.append(u[x])
#将单位字符列表逆序
ulist.reverse()

#结果列表
rlist = []
#合并数字大写字符列表和单位列表
for x in range(len(mlist)):
    #将每个数字字符所对应的大写字符添加到结果列表中
    rlist.append(mlist[x])
    #将每个数字字符所对应的单位字符添加到结果列表中
    rlist.append(ulist[x])
#将结果列表转为字符串输出
res = ''.join(rlist)
print(res)




