#-*-coding:utf-8-*-
import time
from selenium.webdriver.common.by import By
from src.test.page.home_page import HomePage
from utils.config import Config

class OrderListPage (HomePage):
    OrdinaryOrderID = Config().get_config("OrdinaryOrderID",2)
    ParentOrderID = Config().get_config("ParentOrderID",2)
    ChildOrderID = Config().get_config("ChildOrderID",2)
    inputType = (By.XPATH, Config().get_locator("inputType",3))
    viewOrderDetails = (By.XPATH, Config().get_locator("viewOrderDetails",3))
    viewOrderDetails2 = (By.XPATH, Config().get_locator("viewOrderDetails2", 3))
    OrdinaryOrder = (By.XPATH, Config().get_locator("OrdinaryOrder", 3))
    ParentOrder = (By.XPATH, Config().get_locator("ParentOrder", 3))
    viewP2COrder = (By.XPATH,Config().get_locator("viewP2COrder",3))
    ChildOrder = (By.XPATH, Config().get_locator("ChildOrder", 3))
    inputOrderId = (By.XPATH, Config().get_locator("inputOrderId", 3))
    searchButton = (By.XPATH, Config().get_locator("searchButton", 3))
    paymentMethod_select = (By.XPATH, Config().get_locator("paymentMethod_select", 3))
    payment_Paypal = (By.XPATH, Config().get_locator("payment_Paypal", 3))

    # def __init__(self):
    #     self.click_orderList()


    # 测试场景
    def click_viewOrderDetails(self):
        # self.click_orderList ()
        # time.sleep (0.5)
        self.find_element(*self.viewOrderDetails).click()
        time.sleep (3)

    def viewOrdinaryOrderDetails(self):
        # self.click_orderList ()
        # time.sleep (0.5)
        self.find_element(*self.inputType).click()
        time.sleep (0.2)
        self.find_element (*self.OrdinaryOrder).click ()
        self.find_element (*self.inputOrderId).send_keys(Config().get_config("OrdinaryOrderID",2))
        time.sleep (0.2)
        self.find_element (*self.searchButton).click ()
        self.find_element(*self.viewOrderDetails).click()
    def viewParentOrderDetails(self):
        # self.click_orderList ()
        # time.sleep (0.5)
        self.find_element(*self.inputType).click()
        time.sleep (0.5)
        self.find_element (*self.ParentOrder).click ()
        self.find_element (*self.inputOrderId).send_keys(Config().get_config("ParentOrderID",2))
        self.find_element (*self.searchButton).click ()
        time.sleep (0.5)
        self.find_element(*self.viewP2COrder).click()
        time.sleep (2)
        self.find_element (*self.viewOrderDetails).click ()
        self.find_element (*self.viewOrderDetails2).click ()
    def viewChildOrderDetails(self):
        # self.click_orderList ()
        # time.sleep (0.5)
        self.find_element(*self.inputType).click()
        time.sleep (0.5)
        self.find_element (*self.ChildOrder).click ()
        self.find_element (*self.inputOrderId).send_keys(Config().get_config("ChildOrderID",2))
        self.find_element (*self.searchButton).click ()
        time.sleep (2)
        self.find_element(*self.viewOrderDetails).click()
    def viewPaypalOrderDetails(self):
        # self.click_orderList()
        # time.sleep(0.8)
        self.find_element(*self.paymentMethod_select).click()
        self.find_element(*self.payment_Paypal).click()
        self.find_element(*self.searchButton).click()
        time.sleep(3)
        self.find_element(*self.viewOrderDetails).click()





