import cv2
import os
import urllib
import urllib.request

# 加载训练数据集
recognizer = cv2.face.LBPHFaceRecognizer_create()
# 加载数据
recognizer.read('result/trainer.yml')
# 名称
names = []
# 警报全局变量
warningtime = 0
# md5加密
def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()


# 短信反馈
statusStr = {
    '0': '短信发送成功',
    '-1': '参数不全',
    '-2': '服务器空间不支持，请确认支持curl或者fsocket，联系您的空间商解决或者更换空间',
    '30': '密码错误',
    '40': '帐号不存在',
    '41': '余额不足',
    '42': '账户已过期',
    '43': 'IP地址限制',
    '50': '内容含有敏感词'
}

# 报警模块
def warning():
    smsapi = 'http://api.smsbao.com/'
    user = '15700000000'
    password = md5('88888')
    content = 'baojing'
    phone = '15700000000'

    data = urllib.parse.urlencode({'u': user, 'p': password, 'm': phone, 'c': content})
    send_url = smsapi + 'sms?' + data
    response = urllib.request.urlopen(send_url)
    the_page = response.read().decode('utf-8')
    print(statusStr[the_page])

# 准备识别的图片
def face_detect_demo(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier('/media/zhuht/WD5/opencv-master/opencv-master/data/haarcascades'
                                       '/haarcascade_frontalface_alt2.xml')
    face = face_detector.detectMultiScale(gray)

    for x, y, w, h in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=1)
        cv2.circle(img, center=(x+w//2, y+h//2), radius=w//2, color=(0, 255, 0), thickness=1)
        ids, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        if confidence > 80:
            global warningtime
            warningtime += 1
            if warningtime > 100:
                warning()
                warningtime = 0
            cv2.putText(img, 'unknown', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        else:
            cv2.putText(img, str(names[ids - 1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
    cv2.imshow('result', img)
