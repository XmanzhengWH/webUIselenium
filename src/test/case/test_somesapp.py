#-*-coding:utf-8-*-
import time
import unittest
from appium import webdriver


class AppiumTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '5.1.1',  # 系统版本号
                        'deviceName': '127.0.0.1:62001',  # 设备名称。
                        'automationName': 'uiautomator2',
                        'appPackage': 'com.instagram.android',  # apk的包名
                        'appActivity': 'com.instagram.android.activity.MainTabActivity'  # activity 名称
                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(8)


        @classmethod
        def tearDown(self):
            self.driver.quit ()

    def test_click(self, t=500):
        """切换测试"""
        time.sleep(3)
        # self.driver.find_element_by_id ('com.instagram.android:id/tab_icon').click ()
        # self.driver.find_element_by_id('com.instagram.android:id/tab_icon').click()
        self.driver.find_element_by_id('com.instagram.android:id/action_bar_inbox_button').click()
        time.sleep (3)

