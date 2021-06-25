'''电子宠物-挑战包'''
'''stamp:标记修改点,本文共有3个标记'''

#电子宠物金鱼宝宝
#引入random模块，用来取随机数
import random

#金鱼宝宝基本属性
name = 'BoboFish'  #名字
HP = 1000  #初始体力
eggs = 0  #产卵总数
#stamp1:增加衰老系数属性
old = 0 #衰老系数

print('小金鱼' + name + '陪你玩耍！')
#主循环
while True:
    if HP > 2000:
        print('吃的太多，受不了了')
        break
    if HP < 0:
        print('太累了，不行了')
        break
    message = input('要小金鱼' + name + '做什么:')
    #判断语句
    if message == 'eat':  #判断进食
        #stamp2:每次进食衰老系数增加，使得每次进食减少
        old = old + 0.1
        HP = HP + (random.randint(300, 400) * (1 - old))
        print('什么东西，真香')
    elif message == 'lay':  #判断产卵
        #stamp3:每次产卵衰老系数增加，使得每次消耗增大
        old = old + 0.1
        lay = random.randint(10, 20)
        HP = HP + (random.randint(-450, -350) * (1 + old))
        print('产下了' + str(lay) + '颗卵')
        eggs = eggs + lay
    else:
        print('哎？' + name + '不知道这是什么意思呀')
print('产卵总数:' + str(eggs))