import time

import src.driver.DriverCreater as driverCreater
import xlwings as xw
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from src.autoclick import cookie_data

# 创建Chrome对象
driver = driverCreater.onWindows()

def main():
    # xlwings excel读写库
    # 新建excel
    app = xw.App(visible=True, add_book=False)
    file = app.books.add()
    sheet = file.sheets[0]

    # 评论页面
    evaluate = 'https://item.jd.com/100009083138.html#crumb-wrap'
    driver.get(evaluate)
    # time.sleep(3)
    # 获取并点击 商品评价
    # 找到li标签中，有名为 clstag的属性且值为 "shangpin|keycount|product|shangpinpingjia_1" 的元素
    driver.find_element_by_css_selector('li[clstag="shangpin|keycount|product|shangpinpingjia_1"]').click()

    time.sleep(1)
    # 获取并点击 只看当前商品评价
    # . 表示类选择器，查找class= comm-curr-sku 的元素
    curr_li = driver.find_element_by_css_selector('.comm-curr-sku').click()
    # time.sleep(3)

    save_evaluate(sheet)

    file.save('e://data.xlsx')
    app.quit()

    # 使用完关闭浏览器，不然Chromedriver.exe 进程会一直在内存中
    driver.quit()


def page_turn():
    # 获取下一页按钮
    try:
        # 这里按钮没有用.click() 方法，因为没有效果
        next_btn = driver.find_element_by_css_selector(".ui-pager-next").send_keys(Keys.ENTER)
        return True
    except:
        print('没有下一页了。。。。。。。')
        return False


def save_evaluate(sheet):
    # 获取评论用户信息
    row = 1
    while True:
        time.sleep(2)
        try:
            users = driver.find_elements_by_css_selector('.comment-item')
            if len(users) <= 0:
                print('没有评价了')
                break
            for user in users:
                user_info = user.find_element_by_css_selector('.user-info').text
                comment_con = user.find_element_by_css_selector('.comment-con').text
                print(user_info)
                print(comment_con)
                sheet.range('A%d' % row).value = user_info
                sheet.range('B%d' % row).value = comment_con
                row = row + 1
            if not page_turn():
                break
        except:
            print('获取评价时异常')
            break


if __name__ == '__main__':
    main()
