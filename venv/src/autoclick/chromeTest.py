import time

from selenium import webdriver
from src.autoclick import cookie_data

driver_path = 'C:/Users/zhuhaitao/PycharmProjects/path/chromedriver'
# 创建Chrome对象,有界面
# driver = webdriver.Chrome(driver_path)

# 无界面操作
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(executable_path=driver_path, options=option)

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


# 重新发送请求，由于添加了cookie，此时应该是登录状态
driver.get(checkin_url)
time.sleep(3)
# find_element 都只取找到的第一个元素；find_elements 会取出所有符合条件的元素
# 按class名称定为元素，若class中是带空格的多个名称，需要指定其中一个
# btn = driver.find_element_by_class_name('green')
# 按链接的文本内容模糊匹配
# btn = driver.find_element_by_partial_link_text('签到')
# 按元素的绝对路径定位
# btn = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[1]/a')
# 按css 属性定位
btn = driver.find_element_by_css_selector('.btn.green')
print(btn)
# btn.click()

# btn = driver.find_element_by_xpath('/html/body/div[1]/div[1]/a[2]')
# btn.click()

# 使用完关闭浏览器，不然Chromedriver.exe 进程会一直在内存中
# driver.quit()
