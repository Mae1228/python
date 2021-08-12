from PIL import Image
import random

im = Image.open('编程猫剪影.jpg')
width = im.size[0]
height = im.size[1]
area = width * height
total = 10000
count = 0

# 用蒙特卡洛方法获得估计值
for i in range(total):  
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    k = im.getpixel((x, y))
    if k[0] == 0 and k[1] == 0 and k[2] == 0:
        count += 1
print(int(area * count / total))

#以下为选学内容
# count = 0
# # 用遍历所有像素点获得准确值
# for i in range(width):  
#     for j in range(height):
#         k = im.getpixel((i, j))
#         if k[0]== 0 and k[1]== 0 and k[2] == 0:
#             count += 1
# print(count)



