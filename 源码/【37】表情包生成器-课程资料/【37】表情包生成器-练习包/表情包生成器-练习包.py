'''表情包生成器-练习包'''
#Image模块：PIL库基本模块，常与其他模块搭配使用。该模块提供了很多功能，比如加载图像和创建新图像。
#ImageDraw模块：提供了图像对象的简单2D绘制。
#ImageFont模块：与ImageDraw模块的text()方法一起使用，用于设置字体。

#实践一：
from PIL import Image, ImageDraw, ImageFont


#实践二：
#加载图片
im = Image.open('编程猫.png')
#显示图片
im.show()
#保存图片
im.save('编程猫副本.png')


#实践三：
#加载图片
im = Image.open('编程猫.png')
#创建一个绘制im的对象
draw = ImageDraw.Draw(im)
#设置文字的字体和大小
font = ImageFont.truetype('simhei.ttf', 50)
#图片中插入文字
draw.text((0, 200), '这是测试本文！', fill='blue', font=font)
#显示图片
im.show()
#保存图片
im.save('编程猫副本.png')






