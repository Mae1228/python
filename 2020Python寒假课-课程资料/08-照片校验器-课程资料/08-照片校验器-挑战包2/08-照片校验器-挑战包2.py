'''
照片校验器-挑战包2
修改程序将人脸框变成双层，蓝色框里套红色框。
stamp: 标记修改点, 本文共有1个标记
'''

#第一步：导入图像处理工具箱
import cv2

#第二步：读取要处理的图像文件
img = cv2.imread('pic.jpg', 1)

#第三步：识别图像中的人脸数据
face_engine = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
faces = face_engine.detectMultiScale(img, 1.1, 5)

#第四步：处理图像中的人脸数据
for facedata in faces:
    x, y, w, h = facedata
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #stamp1:再次使用绘制矩形框工具，调整起始坐标，从而在内层再绘制一个红色框
    cv2.rectangle(img, (x+5, y+5), (x+w-5, y+h-5), (0, 0, 255), 2)

#第五步：显示图像中的人脸数据
cv2.imshow('showimage', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#第六步：保存处理后的图像为新文件
cv2.imwrite('newpic.jpg', img)















