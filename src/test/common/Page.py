#-*-coding:utf-8-*-
from src.test.common.browser import Browser
from utils.reuseChrome import ReuseChrome


class Page(Browser):
    # 更多的封装请自己动手...
    def __init__(self, page=None, browser_type='firefox'):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)

    def get_driver(self):
        return self.driver

    def reget_driver(self):
        executor_url = self.driver.command_executor._url
        session_id = self.driver.session_id
        driverB = ReuseChrome(command_executor=executor_url, session_id=session_id)
        return driverB

    def refreshPage(self):
        return self.driver.refresh()

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)