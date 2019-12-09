from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver_path = 'C:/Users/zhuhaitao/PycharmProjects/path/chromedriver'

def on_windows() :
    # 创建Chrome对象,有界面
    return webdriver.Chrome(driver_path)

def off_windows():
    # 无界面操作
    option = Options()
    option.add_argument('--headless')  # 浏览器不提供可视化界面，linux下如果系统不支持可视化，不加这条会启动失败
    option.add_argument('--disable-gpu')  #
    option.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片，提升速度
    return webdriver.Chrome(executable_path=driver_path, options=option)

