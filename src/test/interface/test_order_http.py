#-*-coding:utf-8-*-
import unittest
from utils.config import Config, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.assertion import assertHTTPCode
import requests


class TestOrderHTTP(unittest.TestCase):
    URL = Config().get('orderV2')

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='GET')




    def test_orderV2_http(self):
        body = Config().get('orderV2form')
        resp = self.request.post("/", method="POST", data=body, headers={"Content-Type":"application/json"})
        logger.debug(resp.text)
        assertHTTPCode (resp, [200])
        # self.assertIn('百度一下，你就知道', resp.text)

if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='Middle_Api_test', description='接口html报告')
        runner.run(TestOrderHTTP('test_orderV2_http'))