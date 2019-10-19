#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import unittest
import requests
import webbrowser
import urllib.parse


class test_crawler(unittest.TestCase):


#     # 原始 HTML 程式碼
# html_doc = """
# <html><head><title>Hello World</title></head>
# <body><h2>Test Header</h2>
# <p>This is a test.</p>
# <a id="link1" href="/my_link1">Link 1</a>
# <a id="link2" href="/my_link2">Link 2</a>
# <p>Hello, <b class="boldtext">Bold Text</b></p>
# </body></html>
# """

    # @classmethod
    # def setUpClass(self):
    #     self.headers = {'Content-Type':'application/json;charset=UTF-8',
    #                     'User-Agent':'Chrome'
    #                     }

    def test_requests_get001(self):
        # Google 搜尋 URL
        google_url = 'https://www.google.com.tw/search'

        # 查詢參數
        my_params = {'q': '寒流'}

        # 下載 Google 搜尋結果
        r = requests.get(google_url, params=my_params)
        print (r.url)
        webbrowser.open (r.url)

        # 確認是否下載成功
        if r.status_code == requests.codes.ok:
            # 以 BeautifulSoup 解析 HTML 原始碼
            soup = BeautifulSoup (r.text, 'html.parser')

            # 觀察 HTML 原始碼
            # print(soup.prettify())

            # 以 CSS 的選擇器來抓取 Google 的搜尋結果
            items = soup.select ('div.g > h3.r > a[href^="/url"]')
            for i in items:
                # 標題
                print ("標題：" + i.text)
                # 網址
                print ("網址：" + i.get ('href'))