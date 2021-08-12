# 创建变量接受键盘输入
text1=input('请输入第1个字符串：')
text2=input('请输入第2个字符串：')

# 计算长度进行比较
text1Len=len(text1)
text2Len=len(text2)
if text1Len>text2Len:
    print(text1,'>',text2)
elif text1Len<text2Len:
    print(text1,'<',text2)
else:
    # 讲字符串转为字符列表
    text1List=list(text1)
    text2List=list(text2)
    isEqual=True
    for i in range(text1Len):
        #将每个字符转为ascii码
        text1Ascii=ord(text1List[i])
        text2Ascii=ord(text2List[i])
        #判断ascii码大小
        if text1Ascii>text2Ascii:
            print(text1,'>',text2)
            isEqual=False
            break
        elif text1Ascii<text2Ascii:
            print(text1, '<',text2)
            isEqual = False
            break
        if isEqual:
            print(text1,'=',text2)