'''
照片校验器-挑战包1
修改程序将人脸框调整为红色。
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
    #stamp1:人脸框设置为红色（BGR色彩模式）
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

#第五步：显示图像中的人脸数据
cv2.imshow('showimage', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#第六步：保存处理后的图像为新文件
cv2.imwrite('newpic.jpg', img)
