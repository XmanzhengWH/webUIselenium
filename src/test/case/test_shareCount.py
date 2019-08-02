#-*-coding:utf-8-*-
import time
import unittest
from src.test.page.shareCount_page import shareCountPage
from utils.config import Config,DATA_PATH,REPORT_PATH,LOG_PATH
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email


class testShareCount(unittest.TestCase):
    mainUrl = Config().get_config("mainhost",0)
    loginUrl = mainUrl + Config().get_config('loginUrl',0)
    homeUrl = mainUrl + Config().get_config("homeUrl")


    @classmethod
    def setUpClass(self):
        self.page = shareCountPage(browser_type='chrome').get(self.loginUrl, maximize_window=False)
        self.page.login()
        self.page.click_shareCount()
        time.sleep(2)
        return self.page

    @classmethod
    def tearDownClass(self):
        # self.page.logout()
        time.sleep(2)
        self.page.quit()

    def test_refresh(self):
        self.page.refreshPage()
        time.sleep(2)

    def test_sleep(self):
        time.sleep(2)

    def test_Thailand_ProductRanking(self):
        self.page.refreshPage ()
        self.page.click_selectThailand()
        time.sleep (0.5)
        self.page.click_PRviewPV()
        time.sleep(1)
        self.page.click_PRselectUV()
        time.sleep (1)
        self.page.click_PRselectShare()
        time.sleep(1)
        self.page.click_PRselectCreateOrder()
    def test_Thailand_ChannelCount(self):
        self.page.refreshPage()
        self.page.click_selectThailand()
        time.sleep(0.9)
        self.page.click_CCselectAll()
        time.sleep(0.5)
        self.page.click_CCselectCopylink()
        time.sleep(0.5)
        self.page.click_CCselectInstagram()
        time.sleep(0.5)
        self.page.click_CCselectLine()
        time.sleep(0.5)
        self.page.click_CCselectTwitter()
        time.sleep(0.5)
        self.page.click_CCselectFacebook()