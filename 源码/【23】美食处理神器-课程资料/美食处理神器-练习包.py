'''美食处理神器-练习包'''

#调用PIL模块
from PIL import Image

#获取并打印全部的图片像素点信息
#读取图片文件
img = Image.open('steak.jpg')
#获取图片尺寸
width, height = img.size
#加载图片内容
img_array = img.load()
#循环获取RBG颜色数据
for x in range(width):
    for y in range(height):
        print(img_array[x, y])

#将图片全部刷蓝并保存为新图片
#读取图片文件
img = Image.open('steak.jpg')
#获取图片尺寸
width, height = img.size
#加载图片内容
img_array = img.load()
#循环获取RBG颜色数据
for x in range(width):
    for y in range(height):
        img_array[x, y] = (0, 0, 255)
#另存为新的图片
img.save('blue.jpg')