import time

import src.driver.DriverProducer as driverProducer
import xlwings as xw
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from src.autoclick import cookie_data

# 创建Chrome对象,使用本地下载的指定地址的驱动
# 有界面
driver = driverProducer.on_windows()


# 无界面
# driver = driverProducer.off_windows()


# 创建Chrome对象，使用安装的驱动，需要配置环境变量
# driver = webdriver.Chrome()

def main():
    # xlwings excel读写库
    # 新建excel
    app = xw.App(visible=True, add_book=False)
    file = app.books.add()
    sheet = file.sheets[0]

    # 评论页面
    evaluate = 'https://item.jd.com/100009083138.html#crumb-wrap'
    driver.get(evaluate)
    # 进入商品评价页面
    sppj()
    # 保存评价
    save_evaluate(sheet)
    # 保存excel文件
    file.save('e://data.xlsx')
    app.quit()

    # 使用完关闭浏览器，不然Chromedriver.exe 进程会一直在内存中
    driver.quit()


def sppj():
    refresh = 0
    while True:
        try:
            # 获取并点击 商品评价
            # 找到li标签中，有名为 clstag的属性且值为 "shangpin|keycount|product|shangpinpingjia_1" 的元素
            driver.find_element_by_css_selector('li[clstag="shangpin|keycount|product|shangpinpingjia_1"]').click()

            time.sleep(1)
            # 获取并点击 只看当前商品评价
            # . 表示类选择器，查找class= comm-curr-sku 的元素
            driver.find_element_by_css_selector('.comm-curr-sku').click()
            # 正常到这一步后跳出循环继续
            break
        except (NoSuchElementException, ElementClickInterceptedException):
            # 有时候第一次进页面点击 商品评价 时，可能会报这个按钮是不可点击的，或者点击后没有返回的评价数据，暂时不清楚这种情况产生的原因
            if refresh == 3:
                print('无法获取元素,或元素无法点击')
                return
            driver.refresh()
            refresh = refresh + 1


def page_turn():
    # 获取下一页按钮
    try:
        # 这里按钮没有用.click() 方法，因为没有效果
        driver.find_element_by_css_selector(".ui-pager-next").send_keys(Keys.ENTER)
        return True
    except NoSuchElementException:
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
        except NoSuchElementException:
            print('获取评价时异常')
            break


if __name__ == '__main__':
    main()
