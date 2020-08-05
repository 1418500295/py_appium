import unittest
from utils.driverUtil import DriverUtil
from config.logConfig import LogConfig
from pages.video_first_page import VideoFirstPage
from utils.BaseFun import BaseFun

logger = LogConfig.get_log()

class TestCase(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()
        cls.baseFun = BaseFun(cls.driver)
        cls.firstPage = VideoFirstPage()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.implicitly_wait(10)


    def test_01(self):
        self.baseFun.click(self.firstPage.cache_button)
        self.baseFun.key_event_back()
        self.baseFun.save_screenshot("first.png")
        print(self.driver.contexts)
        print(self.driver.current_context,self.driver.current_activity)
        # print(self.driver.page_source)






if __name__ == '__main__':
    unittest.main()