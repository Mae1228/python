'''懵到反色的阿短-成果包'''

#调用PIL模块
from PIL import Image

#反色处理小程序
#读取图片文件
img = Image.open('懵圈阿短.png')
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
        #反色操作
        r = 255 - r
        b = 255 - b
        g = 255 - g
        img_array[x, y] = (r, g, b)
#图片保存
img.save('懵圈阿短反色.png')
