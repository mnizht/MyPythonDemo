#导入cv模块
import cv2 as cv

#检测函数
def face_detect_demo():
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('/media/zhuht/WD5/opencv-master/opencv-master/data/haarcascades'
                                       '/haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(gray, 1.01, 5)

    for x, y, w, h in face:
        cv.rectangle(img, (x, y,), (x+w, y+h), color=(0, 0, 255), thickness=2)
    cv.imshow('result', img)

#读取图像
img = cv.imread('source/trump.png')

#检测函数
face_detect_demo()

#等待,键盘按下q键退出
while True:
    if ord('q') == cv.waitKey(0):
        break

#释放内存
cv.destroyAllWindows()