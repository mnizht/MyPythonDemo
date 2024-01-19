import requests
from bs4 import BeautifulSoup
import time

def crawl_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h3', class_='fl l-name-h3')
        # links = soup.find_all('div', class_='l-attr')

        for title in zip(titles):
            print(f"{title[0].contents[0].contents[0]}|{title[0].contents[0].attrs['href']}")
            # print(f"Link: {link['href']}")
            # print()

def crawl_multiple_pages(base_url, num_pages):
    for page_num in range(1, num_pages + 1):
        url = f"{base_url}pn{page_num}.html?k=购物中心"
        # print(f"Scraping page {page_num} - URL: {url}")
        crawl_page(url)
        time.sleep(2)  # 添加延迟

# 示例使用一个博客网站的 URL，你需要根据实际情况替换为目标网站的 URL
base_url = 'http://baseUrl/xiangmu/s0-c0-t0-r0-g0-x0-d0-z0-n0-m0-l0-q0-b0-y0-'
num_pages_to_scrape = 23  # 设置你想要爬取的页数

crawl_multiple_pages(base_url, num_pages_to_scrape)
