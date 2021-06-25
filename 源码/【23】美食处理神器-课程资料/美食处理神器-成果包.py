'''美食处理神器-成果包'''

#美食图片处理小程序
#调用PIL模块
from PIL import Image

#获取图片文件名
name = input('请输入要处理的图片:')
#读取图片文件
img = Image.open(name)
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
            if r < 200:
                r += 55
            else:
                r = 255
            #将处理后的数据赋值给像素点
            img_array[x, y] = (r, g, b)
#图片保存
img.save(name + '_new.jpg')







