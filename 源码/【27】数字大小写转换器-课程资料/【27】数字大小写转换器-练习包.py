'''数字大小写转换器-练习包'''

#实践一：
l = [
    '零',
    '壹',
    '贰',
    '叁',
    '肆',
    '伍',
    '陆',
    '柒',
    '捌',
    '玖',
]
for i in range(10):
    print(str(i)+":"+l[i])

#实践二：
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

#实践三：
print(m['7'])
print(m['9'])


#实践四：
for i, j in m.items():
    print(i+":"+j)
