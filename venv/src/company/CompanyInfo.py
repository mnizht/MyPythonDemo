import random
import time

import xlwings as xw
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from src.autoclick import cookie_data


def save_info(driver):
    # 获取公司信息
    name = driver.find_element_by_class_name('name').text
    phone = driver.find_element_by_class_name('link-hover-click').text
    email = driver.find_element_by_xpath('//*[@id="company_web_top"]/div[2]/div[3]/div[3]/div[1]/div[2]/span[2]').text
    comapny_url = driver.find_element_by_xpath('//*[@id="company_web_top"]/div[2]/div[3]/div[3]/div[2]/div[1]/span[2]').text
    address = driver.find_element_by_xpath('//*[@id="company_web_top"]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div').text
    owner = driver.find_element_by_xpath('//*[@id="_container_baseInfo"]/table/tbody/tr[1]/td[2]/span').text
    capital = driver.find_element_by_xpath('//*[@id="_container_baseInfo"]/table/tbody/tr[1]/td[4]/div').text


    print('企业 %s 的基本信息===============' %name)
    print('电话：%s' %phone)
    print('邮箱：%s' %email)
    print('网址：%s' %comapny_url)
    print('地址：%s' %address)
    print('法定代表人/负责人：%s' %owner)
    print('注册资本：%s' %capital)



driver_path = 'C:/Users/zhuhaitao/PycharmProjects/path/chromedriver'
# 创建Chrome对象,有界面
driver = webdriver.Chrome(driver_path)

# xlwings excel读写库

# 新建excel
# app = xw.App(visible=True, add_book=False)
# file = app.books.add()
# sheet = file.sheets[0]

# 主页
tyc_company = 'https://www.xxxx.com/company/%s'

# 读取公司信息
companies = ['3189766102','3189766122','3095029848']
for company in companies:
    driver.get(tyc_company %company)
    save_info(driver)

# file.save('e://tyc.xlsx')

# 使用完关闭浏览器，不然Chromedriver.exe 进程会一直在内存中
# driver.quit()
