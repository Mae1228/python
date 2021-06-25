import jieba

sentence = '编程猫超级可爱。'
words = jieba.cut(sentence)
s = '/'.join(words)
print(s)

