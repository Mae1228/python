'''我的英语词典下-工程包'''
import tool

def load_dict():
    '''加载词典'''
    '''
    输入：无
    输出：包含所有单词的字典，格式如{'apple':{'NO.':'1', 'mean': 'n.苹果', 'link': ''}, ......}
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
                'NO.': wordList[0], 'mean': wordList[2] } # 向子典中添加联想词数据
        wordsDict[wordList[1]] = wordDict
    #将存有全部单词信息的wordsDict返回
    return wordsDict


def save_dict():
    '''保存词典'''
    
    


def search_by_ENG(word):
    '''英译中查询'''
    '''
    输入：想要查询的单词word
    输出：单词的对应格式字符串或者没有单词提示字符串res
    '''
    try:
        res = word+'  ' + wordsDict[word]['mean']
        # 判断有无联想词，有则将联想词一块输出
        
    except KeyError:
        res = 'Not found'
    return res


def add_linked_words(word, addWord):
    '''添加联想词'''
    '''
    输入：想要增加的联想词add，被添加的单词word
    输出：更新后的wordsDict
    '''
    
    return wordsDict


def menu():
    '''显示功能菜单'''
    print('-------------------------------')
    print('英译中查找单词功能请按：1')
    #添加联想词功能显示菜单

    print('退出功能请按：0')
    print('-------------------------------')








#主程序
#加载词典
wordsDict = load_dict()
#调用菜单函数
menu()
while True:
    #功能判断
    #选择为0时，退出
    if message == '0':
        #退出时保存词典
    
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
    #选择为2时，添加联想词







