'''
照片校验器-挑战包3
修改程序随机每个人脸框的颜色。
stamp: 标记修改点, 本文共有2个标记
'''

#第一步：导入图像处理工具箱
import cv2
#stamp1:导入随机工具箱
import random

#第二步：读取要处理的图像文件
img = cv2.imread('pic.jpg', 1)

#第三步：识别图像中的人脸数据
face_engine = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
faces = face_engine.detectMultiScale(img, 1.1, 5)

#第四步：处理图像中的人脸数据
for facedata in faces:
    x, y, w, h = facedata
    #stamp2:随机矩形框的颜色
    cv2.rectangle(img, (x, y), (x+w, y+h),
                  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 2)

#第五步：显示图像中的人脸数据
cv2.imshow('showimage', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#第六步：保存处理后的图像为新文件
cv2.imwrite('newpic.jpg', img)














#挑战任务一 ：修改程序将人脸框大小缩小一半，并调整为蓝色（涉及本节内容）

#挑战任务二 ：修改程序将人脸框变成双层，蓝色框里套黄色框（涉及本节内容）

#挑战任务三 ：修改程序随机每张人脸上的人脸框的颜色（涉及random基础和分支）
