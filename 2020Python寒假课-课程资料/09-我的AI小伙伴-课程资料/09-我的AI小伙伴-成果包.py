'''我的AI小伙伴-成果包'''

#第一步：导入爬虫工具箱
import requests

#第二步：定义“问菲菲”函数
def ask_feifei():
    print('这是问菲菲函数') #可删除本行
    #第三步:完善“问菲菲”函数中的“问”
    question = input('我:')
    return question

#第二步：定义“菲菲答”函数
def feifei_answer(question):
    print('这是菲菲答函数')  #可删除本行
    #第三步：完善“菲菲答”函数中的“答”
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
    res = requests.get(url+question)
    html=res.text
    answer = html.split('"')[-2]
    return answer

#第四步：和AI菲菲聊天
print('####你可以和菲菲聊天了！####')
for i in range(10):
    #第二步：实现一问一答
    qst = ask_feifei()
    print('菲菲:' + feifei_answer(qst))
print('####菲菲累了，一会儿再聊吧~####')

