def Convert(text,mode):
    #text需要转换的字符串
    #mode表示转换模式，mode=T则全部转换为大写，为F则全部转换为小写
    newText=''
    textList=list(text)
    for i in range(len(text)):
        ascii=ord(textList[i])
        #转换为大写
        if mode:
            if ascii>=97 and ascii<=122:
                newText+=chr(ascii-32)
            else:
                newText+=textList[i]
        #转换为小写
        else:
            if ascii>=65 and ascii<=90:
                newText+=chr(ascii+32)
            else:
                newText+=textList[i]
    return newText

usertext=input('请输入一个字符串：')
usermode=input('请输入T或F决定大小写：')
print(usertext,'->',Convert(usertext,usermode=='T'))

