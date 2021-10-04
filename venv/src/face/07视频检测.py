#导入cv模块
import cv2 as cv

#检测函数
def face_detect_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('/media/zhuht/WD5/opencv-master/opencv-master/data/haarcascades'
                                       '/haarcascade_frontalface_default.xml')
    face = face_detect.detectMultiScale(gray)

    for x, y, w, h in face:
        cv.rectangle(img, (x, y,), (x+w, y+h), color=(0, 0, 255), thickness=2)
    cv.imshow('result', img)

#读取摄像头
cap = cv.VideoCapture(0)

#没有摄像头就用视频吧
cap = cv.VideoCapture('1.map4')

#等待,键盘按下q键退出
while True:
    flag, frame = cap.read()
    if not flag:
        break

    face_detect_demo(frame)

    # if ord('q') == cv.waitKey(0):
    #     break

#释放内存
cv.destroyAllWindows()
#释放摄像头
cap.release()