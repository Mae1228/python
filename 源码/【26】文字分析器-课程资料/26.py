''''''
'''
jieba分词的原理：利用一个中文词库，确定汉字之间的关联概率；汉字间概率大的组成词组，形成分词结果
jieba分词的三种模式：1、精确模式：把文本精确的切分开，不存在冗余分词
                    2、全模式：把文本中所有可能的词语都扫描出来，有冗余
                    3、搜索引擎模式：在精确模式基础上，多长词再次切分
迭代：遍历
对象：python中一切皆对象，构造任何类型的值都是对象
      三大特性：身份id、类型、值
可迭代对象：可直接用于for循环的对象
            如字符串、列表、集合、元组、字典
jieba.cut(字符串,cut_all=True/False)：返回可迭代对象
                                      cut_all=True：全模式
                                      cut_all=False：精确模式
jieba.lcut(字符串,cut_all)：返回列表
jieba.cut_for_search(字符串)：返回可迭代对象
jieba.lcut_for_search(字符串)：  返回列表
jieba.load_userdict(文件名及路径)：添加指定文件名的词典
                                   文件必须为UTF-8编码
                                   词典的格式：词语 词频（可省） 词性（可省）------空格隔开，顺序不可颠倒
add_word(词,词频,词性)：向字典中添加一个词，词频可省略默认为1，词性可省略
del_word(词)：在词典中删除一个词
sugget_freq(词,tune=True)：调节单个词语的词频，使其能或不能被分出来
jieba.analyse.extract_tags(待提取的文本,topK=20，withWeight=False,allowPos=())：抽取关键词
                                                                                topK：返回几个权重最大的关键词，默认值是20
                                                                                withWeight：是否并返回关键词权重值，默认为False
                                                                                allowPOS：仅包括指定词性的词，默认值为空，即不筛选
'''
'''jieba.cut()方法'''
# import jieba
# # s='我爱编程'
# s='我爱中华人民共和国'
# words=jieba.cut(s)#精确模式
# # words=jieba.cut(s,True)#全模式
# # words=jieba.cut_for_search(s)#搜索引擎模式
# ss='/'.join(words)
# print(ss)


'''练习1'''
# import jieba
# s='编程猫超级可爱'
# # jieba.suggest_freq('编程猫',True)
# words=jieba.cut(s)
# ss='/'.join(words)
# print(ss)


'''练习2'''
# import jieba
# s='编程猫超级可爱'
# jieba.load_userdict('dict.txt')
# words=jieba.cut(s)
# ss='/'.join(words)
# print(ss)


'''练习3'''
# import jieba.analyse
# with open('text.txt','r',encoding='utf-8') as f:
#     s=f.read()
# # print(s)
# words=jieba.analyse.extract_tags(s,10)
# # print(words)
# for i in words:
#     print(i)


'''-------------------------------------------------------'''














































