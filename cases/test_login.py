
import unittest
from utils.driverUtil import DriverUtil
from utils.addPath import AddPath
from  pages.loginpage import LoginPage
from config.logConfig import LogConfig

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = DriverUtil.get_driver()
        self.driver.implicitly_wait(5)
        self.log = LogConfig().get_log()
        self.path = AddPath.add_project_path()



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
            pass
        self.log.info("pass")





if __name__ == '__main__':
    unittest.main()