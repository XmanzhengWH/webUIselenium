#-*-coding:utf-8-*-
import unittest
from src.test.case.test_mathfunc import TestMathFunc

if __name__ == '__main__':
    pass
    """
    # suite = unittest.TestSuite ()
    # suite.addTests (unittest.TestLoader ().loadTestsFromTestCase (TestMathFunc))
    #
    # with open ('UnittestTextReport.txt', 'a') as f:
    #     runner = unittest.TextTestRunner (stream=f, verbosity=2)
    #     runner.run (suite)


report = REPORT_PATH + '\\report.html'
    suite = unittest.TestSuite()
    tests = [TestMainMenu ("test_into_member"), TestMainMenu ("test_into_product"),TestMainMenu ("test_into_shipping")]
    suite.addTests(tests)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(stream=f, verbosity=2, title='OPSHOP_ADMIN_UI_AUTO_Test', description='自定义场景测试报告')
        runner.run(suite)
    e = Email (title='OPSHOP后台UI测试报告',
               message='这是今天的测试报告，请查收！',
               receiver='xxxx@xxxx.com',
               server='smtp.qiye.aliyun.com',    #smtp.mxhichina.com   &  smtp.qiye.aliyun.com
               sender='XXXX@XXxxx.com',
               password='',
               path=report
               )
    e.send()

    # unittest.main (verbosity=2)
    
    reportLog = LOG_PATH + '/UnittestTextReport.txt'
    suite = unittest.TestSuite()
    tests = [TestMainMenu ("test_into_member"), TestMainMenu ("test_into_product"),TestMainMenu ("test_into_shipping")]
    suite.addTests(tests)
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(tests))
    with open(reportLog, 'a') as f:
        runner = unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(suite)
    
# 【1】unittest模块：TestSuite 多个测试用例集合在一起；TestRunner 是来执行测试用例的，测试的结果会保存到TestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息（unittest.TextTestRunner().run(suite)）
# 
# 【2】suite.addTests（）和suite.addTest（）均可实现
# 
# # 2种用法：第一种suite.addTest()
# suite.addTest(Case('test_case01'))
# suite.addTest(Case('test_case02'))
# suite.addTest(Test('test_01'))
# suite.addTest(Test('test_02'))
# 
# #2种用法：第二种suite.addTests()
# suite.addTests(map(Test, ["test_01", "test_02"]))
# suite.addTests(map(Case, ["test_case01", "test_case02"]))
    
    
    
    """

