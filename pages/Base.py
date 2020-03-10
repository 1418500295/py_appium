

"""
所有类的基类
所有的页面类必须继承此类
"""
class Base(object):

    def __init__(self, driver):
        self.driver = driver
    """
    定位方法封装
    """
    def by_id(self, loc):
        return self.driver.find_element_by_id(loc)

    def by_name(self, loc):
        return self.driver.find_element_by_name(loc)


    def by_xpath(self, loc):
        return self.driver.find_element_by_xpath(loc)


    def by_android_uiautomator(self, loc):
        return self.driver.find_element_by_android_uiautomator(loc)

