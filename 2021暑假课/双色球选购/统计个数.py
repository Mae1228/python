'''
输入一行字符，分别统计出其中英文字母、空额、数字和其他字符的个数


'''
s=input('请输入一个字符串：').strip()
letters=space=digit=other=0
for i in s:
    if i.isalpha():     #判断是否是字母
        letters+=1
    elif i.isspace():   #判断是否是空白字符
        space+=1
    elif i.isdigit():   #判断是否是数字
        digit+=1
    else:
        other+=1
print('字母=',letters,'个，空白字符=',space,'个，数字=',digit,'个，其他=',other,'个',sep='')






