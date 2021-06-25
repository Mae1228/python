'''我的AI小伙伴-挑战1'''

import requests

def ask_feifei():
    question = input('我:')
    return question

def feifei_answer(question):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
    res = requests.get(url+question)
    html=res.text
    answer = html.split('"')[-2]
    return answer

#彩蛋函数
def easter_egg():
    print('Surprise！彩蛋！')

print('####你可以和菲菲聊天了！####')
for i in range(10):
    qst = ask_feifei()
    #如果键入“彩蛋”就调用彩蛋函数，否则就调用菲菲答函数
    if qst == '彩蛋':
        easter_egg()
    else:
        print('菲菲:' + feifei_answer(qst))
print('####菲菲累了，一会儿再聊吧~####')

