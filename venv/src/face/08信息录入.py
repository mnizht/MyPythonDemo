#导入cv模块
import cv2 as cv

#摄像头
cap = cv.VideoCapture(0)

flag = 1
num = 1

while(cap.isOpened()): #检测是否开启
    ret_flag, vShow = cap.read() #得到图片
    cv.imshow('Capture_Test',vShow)
    k = cv.waitKey(1) & 0xff #按键判断
    if k == ord('s'): #保存
        cv.imwrite('source/to/'+str(num)+'.name.jpg', vShow)
        print('success to save'+str(num)+'.jpg')
        print('----------------------')
        num += 1
    elif k == ord(' '):
        break

#释放内存
cv.destroyAllWindows()
#释放摄像头
cap.release()