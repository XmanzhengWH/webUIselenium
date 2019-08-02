#-*-coding:utf-8-*-
from selenium.webdriver.common.by import By

from src.test.page.home_page import OpAdminHomePage
import time

class ShippingPage(OpAdminHomePage):
    ship_manage =(By.CSS_SELECTOR,"#tab-manage")
    ship_templape = (By.CSS_SELECTOR, "#tab-template")

    def click_ship_manage(self):
        self.find_element(*self.ship_manage).click()

    def click_ship_templape(self):
        self.find_element(*self.ship_templape).click()