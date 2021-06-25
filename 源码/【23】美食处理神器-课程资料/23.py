''''''
'''
像素：组成图片的最小单位，单色的正方形的小格子
      每个像素包含3个字节的信息：（R,G,B）
img.open('文件名')：读取图片文件
img.load()：加载图片文件，接收像素数据
rgb色彩：按照色光三原色来设计。亮度范围是0-255,0代表最暗，255代表最亮
img.size：图片尺寸。第一个参数是宽度，第二个参数是高度
img.height：图片的高度
img.width：图片的宽度
img.format：图片的格式，如png
img.mode：图片的模式，如
img.getpixel(x,y)：读取某点的像素信息
tuple元组：有序，可以通过索引找到向对应的数据。
            元组不可变，可以调用数据但是不能对元组本身进行修改
            t=(1,)
img.show()：将图像保存到临时文件并调用实用程序来显示图像
img.save('新的文件名')
max(a,b,c)：比较多个数据返回最大值
min(a,b,c)：比较多个数据返回最小值
'''
'''实践一'''
# from PIL import Image
# img=Image.open('steak.jpg')
# img_array=img.load()
# print(img_array)
# print(img_array[0,0])
# print(img_array[2,2])


'''实践二'''
# from PIL import Image
# img=Image.open('steak.jpg')
# img_array=img.load()
# width,height=img.size
# print(width,height)
# for x in range(width):
#     for y in range(height):
#         print(img_array[x,y])



'''元组'''
# # t=(1)   错误
# t=(1,)
# t=(1,2,3,4,5)
# t=tuple()
# t=()



'''实践三'''
# from PIL import Image
# img=Image.open('steak.jpg')
# img_array=img.load()
# width,height=img.size
# img_array[0,0]=(255,255,255)
# img.show()


'''实践四'''
# from PIL import Image
# img=Image.open('steak.jpg')
# img_array=img.load()
# width,height=img.size
# for x in range(width):
#     for y in range(height):
#         img_array[x,y]=(0,0,255)
# img.save('steak1.jpg')



'''项目'''
# from PIL import Image
# img=Image.open('steak.jpg')
# img_array=img.load()
# width,height=img.size
# for x in range(width):
#     for y in range(height):
#         r=img_array[x,y][0]
#         g=img_array[x,y][1]
#         b=img_array[x,y][2]
#         s=max(r,g,b)
#         if s==r:
#             if s<200:
#                 r+=55
#             else:
#                 r=255
#             img_array[x,y]=(r,g,b)
# img.save('steak0.jpg')


'''----------------------------------------------------------------------------------------------'''


















































