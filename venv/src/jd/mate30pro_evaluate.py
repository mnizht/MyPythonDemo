import time
from selenium import webdriver
from src.autoclick import cookie_data
from selenium.webdriver.common.keys import Keys
import xlwings as xw


def save_evaluate (page,size):
    # 获取评论用户信息
    try:
        users = driver.find_elements_by_class_name('comment-item')
        print(len(users))
        row = page * size + 1
        for user in users:
            print(user.find_element_by_class_name('user-info').text)
            sheet.range('A%d' % row).value = user.find_element_by_class_name('user-info').text
            sheet.range('B%d' % row).value = user.find_element_by_class_name('comment-con').text
            row = row + 1
    except:
        print('没有评价')

driver_path = 'C:/Users/zhuhaitao/PycharmProjects/path/chromedriver'
# 创建Chrome对象,有界面
driver = webdriver.Chrome(driver_path)

# xlwings excel读写库

# 新建excel
app = xw.App(visible=True,add_book=False)
file = app.books.add()
sheet = file.sheets[0]


# 无界面操作
# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# driver = webdriver.Chrome(executable_path=driver_path, options=option)

# 评论页面
evaluate = 'https://item.jd.com/100004788075.html'
driver.get(evaluate)
# 获取并点击 商品评价
evaluate_btn = driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[5]')
evaluate_btn.click()
time.sleep(2)
# 获取并点击 只看当前商品评价
curr = None
try:
    curr = driver.find_element_by_id('comm-curr-sku')
except:
    driver.refresh()
    time.sleep(1)
    curr = driver.find_element_by_id('comm-curr-sku')

curr.send_keys(Keys.ENTER)
time.sleep(1)

page = 0
size = 10
while True:
    # 获取下一页按钮
    try:
        btn = driver.find_element_by_class_name("ui-pager-next")
        save_evaluate(page,size)
        page = page + 1
        btn.send_keys(Keys.ENTER)
        time.sleep(1)
    except:
        print('没有下一页了。。。。。。。')
        btn = None

    if btn == None:
        save_evaluate(page,size)
        break

# btn.send_keys(Keys.ENTER)

time.sleep(1)

file.save('e://data.xlsx')
# app.quit()

# 使用完关闭浏览器，不然Chromedriver.exe 进程会一直在内存中
# driver.quit()


