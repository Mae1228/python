'''图像修复工程师-成果包'''

#调用PIL模块
from PIL import Image

#图像修复小程序
#读取图片文件
img = Image.open('损坏的监控图像.png')
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
        #修复操作
        img_array[x, y] = (r, 0, 0)
#图片保存
img.save('图像修复.png')