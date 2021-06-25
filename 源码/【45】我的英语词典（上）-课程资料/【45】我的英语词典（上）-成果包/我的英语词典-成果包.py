'''我的英语词典上-成果包'''


def load_dict():
    '''加载词典'''
    '''
    输入：无
    输出：包含所有单词的字典，格式如{'apple':{'NO.':'1', 'mean': 'n.苹果'}, ......}
    '''
    #建立空字典用来存储加载出来的单词信息
    wordsDict = {}
    #打开词典文件
    with open('wordsSpace.txt', 'r', encoding='utf-8') as w:
            #读取全部数据
            word_list = w.readlines()
    for word in word_list:
        #读取到的信息处理
        wordList = word.split('#')
        wordDict = {
            'NO.': wordList[0], 'mean': wordList[2]}
        wordsDict[wordList[1]] = wordDict
    #将存有全部单词信息的wordsDict返回
    return wordsDict

def search_by_ENG(word):
    '''英译中查询'''
    '''
    输入：想要查询的单词word
    输出：相应单词含义字符串或者没有单词提示字符串res
    '''
    try:
        res = word+'  ' + wordsDict[word]['mean']
    except KeyError:
        res = 'Not found'
    return res


def menu():
    '''显示功能菜单'''
    print('-------------------------------')
    print('英译中查找单词功能请按：1')
    print('退出功能请按：0')
    print('-------------------------------')


#主程序
#加载词典
wordsDict = load_dict()
#调用菜单函数
menu()
while True:
    message = input('请输入想要使用的功能(#查看功能)：')
    #功能判断
    #选择为0时，退出
    if message == '0':
        break
    #选择为#时，呼出菜单
    elif message == '#':
        menu()
    #选择为1时，单词查询
    elif message == '1':
        while True:
            word = input('查找单词(按0返回)：')
            if word == '0':
                break
            res = search_by_ENG(word)
            print(res)

