#-*-coding:utf-8-*-
import time
import unittest
from selenium.webdriver.common.by import By

from src.test.case.test_mainMenu import TestMainMenu
from src.test.page.home_page import HomePage
from src.test.page.orderList_page import OrderListPage
from utils.config import Config,DATA_PATH,REPORT_PATH,LOG_PATH
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email


class testOrderList(unittest.TestCase):
    mainUrl = Config().get_config("mainhost",0)
    loginUrl = mainUrl + Config().get_config('loginUrl',0)
    homeUrl = mainUrl + Config().get_config("homeUrl")
    externalCategoryUrl = mainUrl + Config().get_config("externalCategoryUrl",0)
    excel = DATA_PATH + '/OpAdmin.xlsx'

    @classmethod
    def setUpClass(self):
        self.page = OrderListPage(browser_type='chrome').get(self.loginUrl, maximize_window=False)
        self.page.login()
        self.page.click_orderList()
        return self.page

    @classmethod
    def tearDownClass(self):
        # self.page.logout()
        time.sleep(2)
        self.page.quit()


    """view OrderDetails"""
    def test_into_viewOrderDetails(self):
        self.page.click_viewOrderDetails()
    def test_viewOrdinaryOrderDetails(self):
        self.page.viewOrdinaryOrderDetails()
    def test_viewParentOrderDetails(self):
        self.page.viewParentOrderDetails()
    def test_viewChildOrderDetails(self):
        self.page.viewChildOrderDetails()
    def test_viewPaypalOrderDetails(self):
        self.page.viewPaypalOrderDetails()


if __name__ == '__main__':
    # unittest.main (verbosity=2)
    report = REPORT_PATH + '\\report.html'

    topmenu = [
        TestMainMenu ("test_into_opshopImg"),
        TestMainMenu ("test_into_member"),
        TestMainMenu ("test_into_product"),
        TestMainMenu ("test_into_order"),
        TestMainMenu ("test_into_datastatistics"),
        TestMainMenu ("test_into_couponList"),
        TestMainMenu ("test_into_operation"),
        TestMainMenu ("test_into_dictionary"),
        TestMainMenu ("test_into_setting"),
        TestMainMenu ("test_into_backend"),
        TestMainMenu ("test_into_imagesearch")
             ]
    secondMenu = [



    ]
    testTemp= [
        # testOrderList("test_viewOrdinaryOrderDetails"),
        # testOrderList ("test_viewParentOrderDetails"),
        testOrderList("test_viewChildOrderDetails")


    ]
    suite1 = unittest.TestSuite ()
    suite1.addTests(topmenu)
    suite2 = unittest.TestSuite ()
    suite2.addTests (secondMenu)
    suite3 = unittest.TestSuite ()
    suite3.addTests (testTemp)

    alltests = unittest.TestSuite ((suite1, suite3))
    # alltests = unittest.TestSuite(suite3)

    # suite.addTests (unittest.TestLoader ().loadTestsFromTestCase (TestMainMenu))
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(stream=f, verbosity=2, title='OPSHOP_ADMIN_UI_AUTO_Test', description='自定义场景测试报告')
        runner.run(alltests)

