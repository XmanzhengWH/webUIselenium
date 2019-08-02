#-*-coding:utf-8-*-
"""
from selenium.webdriver.common.by import By
from src.test.common.Page import Page
from utils.config import Config
import time

class LoginPage(Page):
    Uname = Config().get('Uname')
    Pwd = Config().get('Pwd')
    username_input = (By.CSS_SELECTOR, '.el-form-item:nth-child(2) .el-input__inner')
    password_input = (By.CSS_SELECTOR, '.el-input-group > .el-input__inner')
    login_button = (By.CSS_SELECTOR, '.login-btn')
    clear_button = (By.CSS_SELECTOR, '.el-icon-circle-close')
    clear_button2 = (By.XPATH,"//div[@id='app']/div/form/div[2]/div/div/span[2]/span/i")
    see_pd_button = (By.CSS_SELECTOR, '.fa-eye-slash')
    click_form = (By.CSS_SELECTOR, '.el-form')
    peson_down = (By.CSS_SELECTOR, '.el-down')
    logout_button = (By.CSS_SELECTOR, '.el-dropdown-menu__item:nth-child(3)')

    def login(self):
        # 登录
        self.find_element(*self.username_input).send_keys(self.Uname)
        self.find_element(*self.clear_button).click()
        self.find_element(*self.username_input).send_keys(self.Uname)
        self.find_element(*self.password_input).send_keys(self.Pwd)
        time.sleep (1)
        self.find_element (*self.clear_button2).click ()
        self.find_element(*self.password_input).send_keys(self.Pwd)
        self.find_element (*self.see_pd_button).click ()
        self.find_element (*self.click_form).click()
        self.find_element(*self.login_button).click()
        time.sleep (1)

    def logout(self):
        # 注销账号
        self.find_element (*self.peson_down).click ()
        time.sleep (2)
        self.find_element (*self.logout_button).click ()


        """





