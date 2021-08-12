text=input('请输入单词：')
textList=list(text)
textLen=len(textList)
isHWZ=True
for i in range(textLen//2):
    #过程检测
    if textList[i]!=textList[textLen-i-1]:
        isHWZ=False
        break

#判断输出
if isHWZ==True:
    print(text,'是回文字')
else:
    print(text,'不是回文字')