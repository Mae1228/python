'''表情包生成器-成果包'''
from PIL import Image, ImageDraw, ImageFont
import easygui as g

#通过多文本输入框获得表情包处理信息
msg = "请填写信息"
title = "表情包生成器"
fieldNames = ["原图片(含后缀)", "另存为(含后缀)", "添加文字",
                "文字大小", "文字位置(x轴)", "文字位置(y轴)"]
fieldValues = g.multenterbox(msg, title, fieldNames)
imgIn = fieldValues[0]
imgOut = fieldValues[1]
words = fieldValues[2]
wordSize = int(fieldValues[3])
wordX = int(fieldValues[4])
wordy = int(fieldValues[5])

#加载图片
im = Image.open(imgIn)
#创建一个绘制im的对象
draw = ImageDraw.Draw(im)
#设置文字的字体和大小
font = ImageFont.truetype('simhei.ttf', wordSize)
#图片中插入文字
draw.text((wordX, wordy), words, fill='red', font=font)
#显示图片
im.show()
#保存图片
im.save(imgOut)


