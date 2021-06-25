'''美食处理神器-挑战包'''
'''stamp:标记修改点,本文共有1个标记'''

#美食图片处理小程序
#调用PIL模块
from PIL import Image

#读取图片文件
img = Image.open('steak.jpg')
#获取图片尺寸
width, height = img.size
#加载图片内容
img_array = img.load()
#循环处理像素点
for x in range(width):
    for y in range(height):
        #获取RGB值
        r = img_array[x, y][0]
        g = img_array[x, y][1]
        b = img_array[x, y][2]
        #RGB值处理，红色增强
        if r == max(r, g, b):
            #stamp1:调整增强比例，如果已经非常红，则少调一些
            if r - g < 50 and r - b < 50:
                #不是很红，按照原方案调整
                if r < 200:
                    r += 55
                else:
                    r = 255
                img_array[x, y] = (r, g, b)
            else:
                #判断相对较红，减少调整
                if r < 225:
                    r += 30
                else:
                    r = 255
                img_array[x, y] = (r, g, b)
#图片保存
img.save('steak1.jpg')
