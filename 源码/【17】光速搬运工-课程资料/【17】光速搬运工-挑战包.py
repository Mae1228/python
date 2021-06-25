'''光速搬运工-挑战包'''

#图片复制操作(仅上半部分)
with open('房子.png', 'rb') as p:
    pic = p.read()
with open('B://房子挑战-副本.png', 'wb') as p2:
    p2.write(pic[:len(pic)//2])