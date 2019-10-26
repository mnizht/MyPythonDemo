import time
from selenium import webdriver
from src.autoclick import cookie_data
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import xlwings as xw
import src.driver.DriverCreater as driverCreater

# 创建Chrome对象
driver = driverCreater.offWindows()

def main():

    # xlwings excel读写库
    # 新建excel
    app = xw.App(visible=True, add_book=False)
    file = app.books.add()
    sheet = file.sheets[0]

    # 评论页面
    evaluate = 'https://item.jd.com/100008476860.html'
    driver.get(evaluate)
    time.sleep(2)
    # 获取并点击 商品评价
    evaluate_btn = driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[4]')
    ActionChains(driver).move_to_element(evaluate_btn).click(evaluate_btn).perform()
    time.sleep(2)
    # 获取并点击 只看当前商品评价
    curr = driver.find_element_by_id('comm-curr-sku')
    print('curr: %s' %curr)
    ActionChains(driver).move_to_element(curr).click(curr).perform()
    time.sleep(2)

    page_turn()

    file.save('e://data2.xlsx')
    app.quit()

    # 使用完关闭浏览器，不然Chromedriver.exe 进程会一直在内存中
    driver.quit()

def page_turn():
    page = 0
    size = 10
    while True:
        # 获取下一页按钮
        try:
            next_btn = driver.find_element_by_class_name("ui-pager-next")
            save_evaluate(page, size)
            page = page + 1
            ActionChains(driver).click(next_btn)
            time.sleep(1)
        except:
            input('没有下一页了。。。。。。。')
            next_btn = None

        if next_btn == None:
            save_evaluate(page, size)
            break

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

if __name__ == '__main__':
    main()

