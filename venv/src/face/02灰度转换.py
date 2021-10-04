#导入cv模块
import cv2 as cv

#读取图片
img = cv.imread('source/22_1.jpg')

#灰度转换
gray_img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

#显示灰度
cv.imshow('gray',gray_img)
#保存灰度图片
cv.imwrite('source/to/gray_22_1.jpg',gray_img)

#显示图片
cv.imshow('read_img',img)

#等待
cv.waitKey(0)

#释放内存
cv.destroyAllWindows()