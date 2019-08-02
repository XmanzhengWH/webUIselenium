#-*-coding:utf-8-*-
import time
from selenium.webdriver.common.by import By
from src.test.common.Page import Page
from utils.config import Config



class HomePage(Page):
    """login"""
    Uname = Config ().get_config ('Uname',0)
    Pwd = Config ().get_config ('Pwd',0)
    username_input = (By.CSS_SELECTOR, Config().get_locator("username_input",0))
    password_input = (By.CSS_SELECTOR, Config().get_locator("password_input",0))
    login_button = (By.CSS_SELECTOR, Config().get_locator("login_button",0))
    clear_button = (By.XPATH, Config().get_locator("clear_button",0))
    clear_button2 = (By.XPATH, Config().get_locator("clear_button2",0))
    see_pd_button = (By.CSS_SELECTOR, Config().get_locator("see_pd_button",0))
    click_form = (By.CSS_SELECTOR, Config().get_locator("click_form",0))
    peson_down = (By.XPATH,Config().get_locator("peson_down",0))
    logout_button = (By.XPATH, Config().get_locator("logout_button",0))

    """home_menu"""
    opshopImg = (By.CSS_SELECTOR,Config().get_locator("opshopImg",1))
    member = (By.XPATH,Config().get_locator("member",1))
    product = (By.XPATH,Config().get_locator("product",1))
    order = (By.XPATH,Config().get_locator("order",1))
    imagesearch = (By.XPATH,Config().get_locator("imagesearch",1))
    datastatistics = (By.XPATH,Config().get_locator("datastatistics",1))
    couponList = (By.XPATH,Config().get_locator("couponList",1))
    operation = (By.XPATH,Config().get_locator("operation",1))
    dictionary = (By.XPATH,Config().get_locator("dictionary",1))
    settings = (By.XPATH, Config().get_locator("settings",1))
    backend = (By.XPATH,Config().get_locator("backend",1))

    """menber模块"""
    menberlist = (By.XPATH,Config().get_locator("memberlist",2))
    mymenber = (By.XPATH,Config().get_locator("mymember",2))
    memberReview = (By.XPATH,Config().get_locator("memberReview",2))
    """product模块"""
    productlist = (By.XPATH, Config ().get_locator ("productlist", 2))
    productSpecification = (By.XPATH, Config ().get_locator ("productSpecification", 2))
    productAttribute = (By.XPATH, Config ().get_locator ("productAttribute", 2))
    productCollection = (By.XPATH, Config ().get_locator ("productCollection", 2))
    productStore = (By.XPATH, Config ().get_locator ("productStore", 2))
    productPreQc = (By.XPATH, Config ().get_locator ("productPreQc", 2))
    """Order模块"""
    orderList = (By.XPATH,Config().get_locator("orderList",2))
    orderReview = (By.XPATH,Config().get_locator("orderReview",2))
    abnormalOrder = (By.XPATH,Config().get_locator("abnormalOrder",2))
    """dataManage模块"""
    couponStatistics = (By.XPATH,Config().get_locator("couponStatistics",2))
    PromotionStatistics = (By.XPATH,Config().get_locator("PromotionStatistics",2))
    shareCount = (By.XPATH,Config().get_locator("shareCount",2))
    """operation模块"""
    frontendCategory = (By.XPATH,Config().get_locator("frontendCategory",2))
    homepageSettings = (By.XPATH,Config().get_locator("homepageSettings",2))
    guidePage = (By.XPATH,Config().get_locator("guidePage",2))
    pushMessage = (By.XPATH,Config().get_locator("pushMessage",2))
    """setting模块"""
    externalCategory = (By.XPATH,Config().get_locator("externalCategory",2))
    areaManage =(By.XPATH,Config().get_locator("areaManage",2))
    countryList = (By.XPATH, Config ().get_locator ("countryList", 2))
    currencyList = (By.XPATH, Config ().get_locator ("currencyList", 2))
    freightList = (By.XPATH, Config ().get_locator ("freightList", 2))
    baseCategory = (By.XPATH, Config ().get_locator ("baseCategory", 2))
    shipping = (By.XPATH, Config ().get_locator ("shipping", 2))
    specialCategory = (By.XPATH, Config ().get_locator ("specialCategory", 2))


    """Backend模块"""
    dataDictionary = (By.XPATH,Config().get_locator("dataDictionary",2))
    userlist = (By.XPATH, Config().get_locator("userlist",2))
    rolemanage = (By.XPATH, Config().get_locator("rolemanage",2))
    menumanage = (By.XPATH, Config().get_locator("menumanage",2))
    operationLogs = (By.XPATH, Config().get_locator("operationLogs",2))



    def login(self):
        """登录"""
        self.find_element(*self.username_input).send_keys(self.Uname)
        self.find_element(*self.clear_button).click()
        self.find_element(*self.username_input).send_keys(self.Uname)
        self.find_element(*self.password_input).send_keys(self.Pwd)
        time.sleep (0.5)
        self.find_element (*self.clear_button2).click ()
        self.find_element(*self.password_input).send_keys(self.Pwd)
        self.find_element (*self.see_pd_button).click ()
        self.find_element (*self.click_form).click()
        self.find_element(*self.login_button).click()
        time.sleep (0.5)
    def logout(self):
        """注销账号"""
        self.find_element(*self.peson_down).click()
        time.sleep(1)
        self.find_element(*self.logout_button).click()

    """菜单主模块"""
    def click_opshopImg(self):
        self.find_element(*self.opshopImg).click()
    def click_member(self):
        self.find_element(*self.member).click()
    def click_product(self):
        self.find_element(*self.product).click()
    def click_order(self):
        self.find_element(*self.order).click()
    def click_imagesearch(self):
        self.find_element(*self.imagesearch).click()
    def click_datastatistics(self):
        self.find_element(*self.datastatistics).click()
    def click_couponList(self):
        self.find_element(*self.couponList).click()
    def click_operation(self):
        self.find_element (*self.operation).click ()
    def click_dictionary(self):
        self.find_element (*self.dictionary).click ()
    def click_settings(self):
        self.find_element (*self.settings).click ()
    def click_backend(self):
        self.find_element (*self.backend).click ()

    """member模块"""
    def click_memberlist(self):
        self.click_member()
        time.sleep (0.5)
        self.find_element(*self.menberlist).click()
    def click_mymember(self):
        self.click_member()
        time.sleep (0.5)
        self.find_element(*self.mymenber).click()
    def click_memberReview(self):
        self.click_member()
        time.sleep (0.5)
        self.find_element(*self.memberReview).click()

    """product模块"""
    def click_productlist(self):
        self.click_product()
        time.sleep(0.5)
        self.find_element(*self.productlist).click()
    def click_productSpecification(self):
        self.click_product()
        time.sleep(0.5)
        self.find_element(*self.productSpecification).click()
    def click_productAttribute(self):
        self.click_product()
        time.sleep(0.5)
        self.find_element(*self.productAttribute).click()
    def click_productCollection(self):
        self.click_product()
        time.sleep(0.5)
        self.find_element(*self.productCollection).click()
    def click_productStore(self):
        self.click_product()
        time.sleep(0.5)
        self.find_element(*self.productStore).click()
    def click_productPreQc(self):
        self.click_product()
        time.sleep(0.5)
        self.find_element(*self.productPreQc).click()

    """Order模块"""
    def click_orderList(self):
        self.click_order()
        time.sleep(0.5)
        self.find_element(*self.orderList).click()
    def click_orderReview(self):
        self.click_order()
        time.sleep(0.5)
        self.find_element(*self.orderReview).click
    def click_abnormalOrder(self):
        self.click_order()
        time.sleep(0.5)
        self.find_element(*self.abnormalOrder).click()

    """dataManage模块"""
    def click_couponStatistics(self):
        self.click_datastatistics()
        time.sleep(0.5)
        self.find_element(*self.couponStatistics).click()
    def click_PromotionStatistics(self):
        self.click_datastatistics()
        time.sleep(0.5)
        self.find_element(*self.PromotionStatistics).click()
    def click_shareCount(self):
        self.click_datastatistics()
        time.sleep(0.5)
        self.find_element(*self.shareCount).click()
    """operation模块"""
    def click_frontendCategory(self):
        self.click_operation()
        time.sleep(0.5)
        self.find_element(*self.frontendCategory).click()
    def click_homepageSettings(self):
        self.click_operation()
        time.sleep(0.5)
        self.find_element(*self.homepageSettings).click()
    def click_guidePage(self):
        self.click_operation()
        time.sleep(0.5)
        self.find_element(*self.guidePage).click()
    def click_pushMessage(self):
        self.click_operation()
        time.sleep(0.5)
        self.find_element(*self.pushMessage).click()

    """setting模块"""
    def click_shipping(self):
        self.click_settings()
        time.sleep (0.5)
        self.find_element(*self.shipping).click()
    def click_externalCategory(self):
        self.click_settings()
        time.sleep(0.5)
        self.find_element(*self.externalCategory).click()
    def click_areaManage(self):
        self.click_settings()
        time.sleep (0.5)
        self.find_element(*self.areaManage).click()
    def click_countryList(self):
        self.click_settings()
        time.sleep(0.5)
        self.find_element(*self.countryList).click()
    def click_currencyList(self):
        self.click_settings()
        time.sleep(0.5)
        self.find_element(*self.currencyList).click()
    def click_freightList(self):
        self.click_settings()
        time.sleep(0.5)
        self.find_element(*self.freightList).click()
    def click_baseCategory(self):
        self.click_settings()
        time.sleep(0.5)
        self.find_element(*self.baseCategory).click()
    def click_specialCategory(self):
        self.click_settings()
        time.sleep(0.5)
        self.find_element(*self.specialCategory).click()
    """Backend模块"""
    def click_dataDictionary(self):
        self.click_backend()
        time.sleep(0.5)
        self.find_element(*self.dataDictionary).click()
    def click_userlist(self):
        self.click_backend()
        time.sleep(0.5)
        self.find_element(*self.userlist).click()
    def click_rolemanage(self):
        self.click_backend()
        time.sleep (0.5)
        self.find_element (*self.rolemanage).click ()
    def click_menumanage(self):
        self.click_backend()
        time.sleep (0.5)
        self.find_element (*self.menumanage).click ()
    def click_operationLogs(self):
        self.click_backend()
        time.sleep (0.5)
        self.find_element (*self.operationLogs).click ()