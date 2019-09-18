import time

from selenium import webdriver
from src.autoclick import cookie_data

# 创建Chrome对象
driver = webdriver.Chrome('C:/Users/zhuhaitao/PycharmProjects/path/chromedriver')
# 签到地址
checkin_url = 'https://hacpai.com/activity/checkin'

driver.get(checkin_url)
for cookie in driver.get_cookies():
    print("%s -> %s" %(cookie['name'],cookie['value']))

print('============================================')
driver.add_cookie({
            'name': 'symphony',
            'value': '1c3c72536bec60bacfb08a23d93dcd2029ab9afe42fc9de4ec2c424a977cc5b87921fb09da53e3dea781d9e3cbb07944b9b6af9cd7a9c59ddd74c78888f2190acfa12b7b5a402e20cbd65b647a74bb497e7af00c8a58f3a79484d7556e0e18fa86dc394cc492307666930819e12862f0b7118fa814ff59'
        })

time.sleep(2)

driver.get(checkin_url)
# 使用完关闭浏览器，不然Chromedriver.exe 进程会一直在内存中
# driver.quit()
