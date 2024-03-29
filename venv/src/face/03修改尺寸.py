#导入cv模块
import cv2 as cv

#读取图片
img = cv.imread('source/22_1.jpg')

#修改尺寸
resize_img = cv.resize(img, dsize=(256, 144))

#显示原图
cv.imshow('img', img)

#显示修改后的尺寸
cv.imshow('resize_img', resize_img)

#打印原图尺寸大小
print('未修改:', img.shape)

#打印修改后的大小
print('修改后：', resize_img.shape)

#等待,键盘按下q键退出
while True:
    if ord('q') == cv.waitKey(0):
        break

#释放内存
cv.destroyAllWindows()