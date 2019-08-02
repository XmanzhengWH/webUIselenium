#-*-coding:utf-8-*-
import time
from selenium.webdriver.common.by import By
from src.test.page.home_page import HomePage
from utils.config import Config


class shareCountPage(HomePage):

    selectCountry = (By.XPATH, Config().get_locator("selectCountry", 4))
    selectThailand = (By.XPATH, Config().get_locator("selectThailand", 4))
    selectIndonesia = (By.XPATH, Config().get_locator("selectIndonesia", 4))
    selectUnitedStates = (By.XPATH, Config().get_locator("selectUnitedStates", 4))
    selectChina = (By.XPATH, Config().get_locator("selectChina", 4))
    selectPakistan = (By.XPATH, Config().get_locator("selectPakistan", 4))

    PRselectIndex = (By.XPATH, Config().get_locator("PRselectIndex", 4))
    PRselectPV = (By.XPATH, Config().get_locator("PRselectPV", 4))
    PRselectUV = (By.XPATH, Config().get_locator("PRselectUV", 4))
    PRselectShare = (By.XPATH, Config().get_locator("PRselectShare", 4))
    PRselectCreateOrder = (By.XPATH, Config().get_locator("PRselectCreateOrder", 4))
    PRsearchPRButton = (By.XPATH, Config().get_locator("PRsearchPRButton", 4))

    CCselectIndex = (By.XPATH, Config().get_locator("CCselectIndex", 4))
    CCselectAll = (By.XPATH, Config().get_locator("CCselectAll", 4))
    CCselectCopylink = (By.XPATH, Config().get_locator("CCselectCopylink", 4))
    CCselectInstagram = (By.XPATH, Config().get_locator("CCselectInstagram", 4))
    CCselectLine = (By.XPATH, Config().get_locator("CCselectLine", 4))
    CCselectTwitter = (By.XPATH, Config().get_locator("CCselectTwitter", 4))
    CCselectFacebook = (By.XPATH, Config().get_locator("CCselectFacebook", 4))
    CCsearchButton = (By.XPATH, Config().get_locator("CCsearchButton", 4))



    """selectCountry"""
    # def click_selectCountry(self):
    #     self.find_element(*self.selectCountry).click()
    def click_selectThailand(self):
        self.find_element(*self.selectCountry).click()
        time.sleep(1)
        self.find_element(*self.selectThailand).click()
    def click_selectIndonesia(self):
        self.find_element(*self.selectCountry).click()
        self.find_element(*self.selectIndonesia).click()
    def click_selectUnitedStates(self):
        self.find_element (*self.selectCountry).click ()
        self.find_element (*self.selectUnitedStates).click ()
    def click_selectChina(self):
        self.find_element (*self.selectCountry).click ()
        self.find_element (*self.selectChina).click ()
    def click_selectPakistan(self):
        self.find_element (*self.selectCountry).click ()
        self.find_element (*self.selectPakistan).click ()
    """Product Ranking"""
    def click_PRviewPV(self):
        self.find_element (*self.PRselectIndex).click ()
        time.sleep(0.5)
        self.find_element (*self.PRselectPV).click ()
        self.find_element (*self.PRsearchPRButton).click ()
    def click_PRselectUV(self):
        self.find_element (*self.PRselectIndex).click ()
        time.sleep (0.5)
        self.find_element (*self.PRselectUV).click ()
        self.find_element (*self.PRsearchPRButton).click ()
    def click_PRselectShare(self):
        self.find_element (*self.PRselectIndex).click ()
        time.sleep (0.5)
        self.find_element (*self.PRselectShare).click ()
        self.find_element (*self.PRsearchPRButton).click ()
    def click_PRselectCreateOrder(self):
        self.find_element (*self.PRselectIndex).click ()
        time.sleep (0.5)
        self.find_element (*self.PRselectCreateOrder).click ()
        self.find_element (*self.PRsearchPRButton).click ()
    """ChannelCount"""
    def click_CCselectAll(self):
        self.find_element(*self.CCselectIndex).click()
        time.sleep(0.8)
        self.find_element(*self.CCselectAll).click()
        self.find_element(*self.CCsearchButton).click()
    def click_CCselectCopylink(self):
        self.find_element (*self.CCselectIndex).click ()
        time.sleep (0.5)
        self.find_element (*self.CCselectCopylink).click ()
        self.find_element (*self.CCsearchButton).click ()
    def click_CCselectInstagram(self):
        self.find_element (*self.CCselectIndex).click ()
        time.sleep (0.5)
        self.find_element (*self.CCselectInstagram).click ()
        self.find_element (*self.CCsearchButton).click ()
    def click_CCselectLine(self):
        self.find_element (*self.CCselectIndex).click ()
        time.sleep (0.5)
        self.find_element (*self.CCselectLine).click ()
        self.find_element (*self.CCsearchButton).click ()
    def click_CCselectTwitter(self):
        self.find_element (*self.CCselectIndex).click ()
        time.sleep (0.5)
        self.find_element (*self.CCselectTwitter).click ()
        self.find_element (*self.CCsearchButton).click ()
    def click_CCselectFacebook(self):
        self.find_element (*self.CCselectIndex).click ()
        time.sleep (0.5)
        self.find_element (*self.CCselectFacebook).click ()
        self.find_element (*self.CCsearchButton).click ()

