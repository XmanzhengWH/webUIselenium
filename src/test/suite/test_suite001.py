#-*-coding:utf-8-*-
import time
from datetime import datetime
import unittest

from src.test.case.test_mainMenu import TestMainMenu
from src.test.case.test_orderListPage import testOrderList
from src.test.case.test_shareCount import testShareCount
from utils.config import Config,DATA_PATH,REPORT_PATH,LOG_PATH
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email


if __name__ == '__main__':
    # unittest.main (verbosity=2)
    # nowTime = datetime.now().strftime('%Y%m%d_%H%M%S')
    # report = REPORT_PATH +'\\OpAdm_AutoUItest_Report-'+nowTime+ '.html'
    report = REPORT_PATH + '\\report.html'
    # report = open(file_name, 'wb')

    testTemp = [
        # testOrderList("test_viewOrdinaryOrderDetails"),
        # testOrderList ("test_viewParentOrderDetails"),
        # testOrderList("test_viewChildOrderDetails"),
        # testOrderList("test_viewPaypalOrderDetails"),

    ]
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
        TestMainMenu ("test_into_productlist"),
        TestMainMenu ("test_into_mymember"),
        TestMainMenu ("test_into_productSpecification"),
        TestMainMenu ("test_into_memberReview"),
        TestMainMenu ("test_into_productAttribute"),
        TestMainMenu ("test_into_mymember"),
        TestMainMenu ("test_into_productCollection"),
        TestMainMenu ("test_into_mymember"),
        TestMainMenu ("test_into_productPreQc"),
        TestMainMenu ("test_into_memberlist"),
        TestMainMenu ("test_sleep"),
        TestMainMenu ("test_into_productStore"),
        TestMainMenu ("test_into_orderList"),
        TestMainMenu ("test_into_orderReview"),
        TestMainMenu ("test_into_couponStatistics"),
        TestMainMenu ("test_into_PromotionStatistics"),
        TestMainMenu ("test_into_shareCount"),
        TestMainMenu ("test_into_abnormalOrder"),
        TestMainMenu ("test_into_homepageSettings"),
        TestMainMenu ("test_into_guidePage"),
        TestMainMenu ("test_into_pushMessage"),
        TestMainMenu ("test_into_frontendCategory"),
        TestMainMenu ("test_into_dataDictionary"),
        TestMainMenu ("test_into_userlist"),
        TestMainMenu ("test_into_rolemanage"),
        TestMainMenu ("test_into_menumanage"),
        TestMainMenu ("test_into_operationLogs"),
        TestMainMenu ("test_into_frontendCategory"),
        TestMainMenu ("test_into_externalCategory"),
        TestMainMenu ("test_into_areaManage"),
        TestMainMenu ("test_into_countryList"),
        TestMainMenu ("test_into_currencyList"),
        TestMainMenu ("test_into_freightList"),
        TestMainMenu ("test_into_baseCategory"),
        TestMainMenu ("test_into_shipping"),
        TestMainMenu ("test_into_specialCategory"),

    ]
    orderlist = [
        testOrderList ("test_into_viewOrderDetails"),
        testOrderList ("test_viewOrdinaryOrderDetails"),
        testOrderList ("test_viewParentOrderDetails"),
        testOrderList ("test_viewChildOrderDetails"),
        testOrderList ("test_viewPaypalOrderDetails"),

    ]
    ShareCount = [
        testShareCount ("test_Thailand_ChannelCount"),
        testShareCount ("test_Thailand_ProductRanking"),

    ]

    suite1 = unittest.TestSuite ()
    suite1.addTests (topmenu)
    suite2 = unittest.TestSuite ()
    suite2.addTests (secondMenu)
    suite3 = unittest.TestSuite ()
    suite3.addTests (orderlist)
    suite4 = unittest.TestSuite ()
    suite4.addTests (ShareCount)
    suite99 = unittest.TestSuite ()
    suite99.addTests (testTemp)

    suite_all = [suite1, suite2, suite3, suite4, ]

    alltests = unittest.TestSuite (suite_all)
    # alltests = unittest.TestSuite(suite99)

    # suite.addTests (unittest.TestLoader ().loadTestsFromTestCase (TestMainMenu))
    with open (report, 'wb') as f:
        runner = HTMLTestRunner (stream=f, verbosity=2, title='OPSHOP_ADMIN_UI_AutoTest_Report',
                                 description='自定义场景测试报告')
        runner.run (alltests)
