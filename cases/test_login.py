import time
import unittest
from utils.driverUtil import DriverUtil
from  pages.login_page import LoginPage
from pages.chat_home import ChatPage
from pages.start_chat import StartChat
from config.logConfig import LogConfig



class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = DriverUtil.get_driver()
        self.driver.implicitly_wait(10)
        self.log = LogConfig().get_log()


    def test_login(self):

        # self.driver.find_element_by_id("cn.guoguo.chat:id/edit_phone").send_keys("18849464646")
        # self.driver.find_element_by_id("cn.guoguo.chat:id/tv_login").click()
        #
        # exp_ele = self.driver.find_element_by_id("cn.guoguo.chat:id/more")
        # if exp_ele:
        #     pass

        login = LoginPage(self.driver)
        login.phone("18849464646")
        login.btn()
        # 断言
        exp_ele = self.driver.find_element_by_id("cn.guoguo.chat:id/more")
        if exp_ele:

            self.log.info("pass")

    def test_chat(self):
        try:
            login = LoginPage(self.driver)
            chat_home = ChatPage(self.driver)
            start_chats = StartChat(self.driver)
            login.phone("18849464646")
            login.btn()
            chat_home.more_btn()
            time.sleep(1)
            start_chats.start_chat_loc()
            friend_list = []
            time.sleep(1)
            eles = self.driver.find_elements_by_id(start_chats.friend_list)
            # eles = start_chats.frined_list_select()
            num = 0
            while(num < 4):
                for one in eles:
                    one.click()
                    num+=1
            start_chats.confirm_btn()
            exp_ele = self.driver.find_element_by_id("cn.guoguo.chat:id/notificationTextView")
            if exp_ele:
                self.log.info("pass")
        except Exception as e:
            print("{} not found".format(e))





if __name__ == '__main__':
    unittest.main()