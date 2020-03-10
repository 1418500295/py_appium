from appium import webdriver
from utils.driverUtil import DriverUtil
from pages.Base import Base


class LoginPage(Base):

    """
    登录页面元素展示
    """
    phone_num = ("cn.guoguo.chat:id/edit_phone")

    verify_num = ("cn.guoguo.chat:id/edit_auth_code")

    login_btn = ("cn.guoguo.chat:id/tv_login")


    """
    各按钮功能封装
    """
    def phone(self, phone):
        self.by_id(self.phone_num).send_keys(phone)

    def btn(self):
        self.by_id(self.login_btn).click()


















