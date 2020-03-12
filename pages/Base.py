

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
        try:
            return self.driver.find_element_by_id(loc)
        except Exception as e:
            print(e)

    def by_id_elements(self, loc):
        try:
            return self.driver.find_elements_by_id(loc)
        except Exception as e:
            print(e)



    def by_name(self, loc):
        try:
            return self.driver.find_element_by_name(loc)
        except Exception as e:
            print(e)

    def by_class_name(self, loc):
        try:
            return self.driver.find_element_by_class_name(loc)
        except Exception as e:
            print(e)


    def by_xpath(self, loc):
        try:
            return self.driver.find_element_by_xpath(loc)
        except Exception as e:
            print(e)


    def by_android_uiautomator(self, loc):
        try:
            return self.driver.find_element_by_android_uiautomator(loc)
        except Exception as e:
            print(e)

