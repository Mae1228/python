'''我的英语词典下-挑战包'''
'''stamp:标记修改点,本文共有3个标记'''

from tool import *

def load_dict():
    '''加载词典'''
    '''
    输入：无
    输出：包含所有单词的字典，格式如{'apple':{'NO.':'1', 'mean': 'n.苹果', 'link': ''}, ......}
    '''
    #建立空字典用来存储加载出来的单词信息
    wordsDict = {}
    #打开词典文件
    with open('wordsSpace.txt', 'r',encoding='utf-8') as w:
         #读取全部数据
        word_list = w.readlines()
    for word in word_list:
        #读取到的信息处理
        wordList = word.split('#')
        wordDict = {'NO.': wordList[0], 'mean': wordList[2],
            'link': wordList[3][:-1]} # 向子典中添加联想词数据
        wordsDict[wordList[1]] = wordDict
    #将存有全部单词信息的wordsDict返回
    return wordsDict

def save_dict():
    '''保存词典'''
    
    #将wordsDict中的单词信息全部倒回源文件，覆盖源文件
    with open('wordsSpace.txt', 'w',encoding='utf-8') as w:
        for k, v in wordsDict.items():
            line = v['NO.'] + '#' + k + '#' + v['mean'] + '#' + v['link'] + '\n'
            w.write(line)

def search_by_ENG(word):
    '''英译中查询'''
    '''
    输入：想要查询的单词word、完整的单词字典wordsDict
    输出：单词的对应格式字符串或者没有单词提示字符串res
    '''
    try:
        res = word+'  '+ wordsDict[word]['mean']
        #添加单词查询次数
        if word in times_dict.keys():
            times_dict[word] += 1
        else:
            times_dict[word] = 1
        # 判断有无联想词，有则将联想词一块输出
        if wordsDict[word]['link']:
            res += "  联想词："+wordsDict[word]['link']
    except KeyError:
        res = 'Not found'
    return res

def add_linked_words(word, addWord):
    '''添加联想词'''
    '''
    输入：想要增加的联想词add，被添加的单词word，单词字典wordsDict
    输出：更新后的wordsDict
    '''
    wordsDict[word]['link'] += addWord
    wordsDict[word]['link'] += ','
    return wordsDict

#stamp1:增加删除联想词功能函数
def delete_linked_words(word, deleteWord):
    '''删除联想词'''
    #获取联想词字符串(去掉末尾逗号)
    wordLink = wordsDict[word]['link'][:-1]
    #分割成列表
    l = wordLink.split(',')
    #判断分支
    if deleteWord in l:
        #如果要删除的单词存在，进行处理
        #删除列表中的单词
        l.remove(deleteWord)
        #组成新的字符串(末尾无逗号)
        wordLink = ','.join(l)
        #判断如果联想词字符串不为空，则末尾增加逗号
        if wordLink != '':
            wordLink += ','
        #将修改好的联想词字符串赋值给wordsDict词典
        wordsDict[word]['link'] = wordLink
        #打印成功提示并返回修改后的wordsDict
        print('删除成功')
        return wordsDict
    else:
        #如果要删除的单词不存在，打印失败并返回原词典
        print('未找到单词，删除失败')
        return wordsDict

def menu():
    '''显示功能菜单'''
    print('-------------------------------')
    print('英译中查找单词功能请按：1')
    #添加联想词功能显示菜单
    print('添加联想词功能请按：2')
    #添加绘制单词查询次数图像功能
    print('绘制单词查询次数图像：3')
    #stamp2:修改显示功能菜单
    print('删除联想词功能请按：4')
    print('退出功能请按：0')
    print('-------------------------------')


#加载词典
wordsDict = load_dict()
#调用菜单函数
menu()
#加载单词查询次数文件
times_dict = load_times()
#功能选择主循环
while True:
    message = input('请输入想要使用的功能(#查看功能)：')
    #功能判断
    #选择为0时，退出
    if message == '0':
        #退出时保存词典
        save_dict()
        #退出时，保存单词查询次数
        save_times(times_dict)
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
    elif message == '2':
        word = input('请输入目标单词：')
        addWord = input('请输入添加的联想词：')
        wordsDict = add_linked_words(word, addWord)
        print('添加成功！')
        #选择为3时，绘制单词查询情况图像
    elif message == '3':
        make_pie(times_dict)
        print('单词查询情况.html')
    #stamp3:增加删除功能
    elif message == '4':  # 删除联想词
        word = input('请输入目标单词：')
        deleteWord = input('请输入删除的联想词：')
        wordsDict = delete_linked_words(word, deleteWord)



