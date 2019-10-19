#-*-coding:utf-8-*-
import unittest
import requests
import webbrowser
import urllib.parse
from bs4 import BeautifulSoup
import json

from utils.config import REPORT_PATH
from utils.HTMLTestRunner import HTMLTestRunner


class test_requests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.headers = {'Content-Type':'application/json;charset=UTF-8',
                        'User-Agent':'Chrome'
                        }
        self.host = 'http://172.20.0.195:9092'
        # Token = self.getToken()

    def getToken(self):
        data = {'username': 'admintest', 'password': '123456'}
        response = requests.post(self.host+'/admin/login',data)
        # print(response.json())
        d = response.json()["data"]
        token = d["token"]
        # print (token)
        return token



    def test_getImg(self):
        response = requests.get('https://img.alicdn.com/tfs/TB1QJJsKgTqK1RjSZPhXXXfOFXa-37-37.png')
        with open('coming.png','wb')as f:
            f.write(response.content)

    def test_updatePassword(self):
            Token = self.getToken()
            data = {'password':'123456'}
            response = requests.post(self.host+'/admin/updatePassword',data,headers={'Authorization':Token})
            print(response.json())
            r = response.json()
            self.assertEqual(r['code'],200)

    def test_requests_get001(self):
            keywords = "新款手机壳全包防摔"
            encode_keywords = urllib.parse.quote (keywords)
            keywords2 = "蛋"
            # print(urllib.parse.quote (keywords))
            # print(urllib.parse.unquote(keywords2))

            param = {"keywords":keywords2}
            response = requests.get('https://s.1688.com/selloffer/offer_search.htm',params = param )
            print(response.url)
            print(response.text)
            webbrowser.open(response.url)

    def test_requests_get002(self):
        # Google 搜尋 URL
        google_url = 'https://www.google.com.tw/search'

        # 查詢參數
        my_params = {'q': '寒流'}

        # 下載 Google 搜尋結果
        r = requests.get (google_url, params=my_params)
        print (r.url)
        print((r.text))
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



# if __name__ == '__main__':
#     report = REPORT_PATH + '\\report.html'
#     with open(report, 'wb') as f:
#         runner = HTMLTestRunner(f, verbosity=2, title='Some_Api_test', description='接口html报告')
#         runner.run(test_requests('test_requsts_post001'))
