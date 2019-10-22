import random
import time

import xlwings as xw
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from src.autoclick import cookie_data


def save_evaluate(page, size):
    # 获取公司名称
    try:
        if page > 250:
            return 0
        companies = driver.find_elements_by_class_name('sv-search-company')
        curr_size = len(companies)
        if curr_size <= 0:
            return 0
        print(curr_size)
        row = page * size + 1
        for company in companies:
            name = company.find_element_by_class_name('name').text
            print(name)
            sheet.range('A%d' % row).value = name
            row = row + 1
        return curr_size
    except:
        print('没有找到公司')


driver_path = 'C:/Users/zhuhaitao/PycharmProjects/path/chromedriver'
# 创建Chrome对象,有界面
driver = webdriver.Chrome(driver_path)

# 无界面操作
# option = Options()
# option.add_argument('--headless')  # 浏览器不提供可视化界面，linux下如果系统不支持可视化，不加这条会启动失败
# option.add_argument('--disable-gpu')  #
# option.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片，提升速度
# driver = webdriver.Chrome(executable_path=driver_path, options=option)

# xlwings excel读写库

# 新建excel
app = xw.App(visible=True, add_book=False)
file = app.books.add()
sheet = file.sheets[0]

# 天眼查主页
tyc = 'https://www.tianyancha.com/'
driver.get(tyc)
time.sleep(20)
driver.refresh()
# 输入关键词查询
key_words = '学生教育培训'
input = driver.find_element_by_id('home-main-search')
input.send_keys(key_words)
input.send_keys(Keys.ENTER)

time.sleep(2)

# 读取公司名称
page = 0
size = 20
err_num = 0
while True:
    # 获取下一页按钮

    try:
        next_btn = driver.find_element_by_class_name("-next")
        curr_size = save_evaluate(page, size)
        if curr_size == 0:
            break
        page = page + 1
        next_btn.send_keys(Keys.ENTER)
        time.sleep(random.random() * 2 + 1)
    except:
        print('检查是否有人工验证')
        err_num = err_num + 1
        time.sleep(20)

    if err_num > 5:
        save_evaluate(page, size)
        break
time.sleep(1)

file.save('e://tyc.xlsx')

# 使用完关闭浏览器，不然Chromedriver.exe 进程会一直在内存中
# driver.quit()
