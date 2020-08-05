import time

from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains

class BaseFun(object):

    def __init__(self, driver):
        self.driver = driver

    # 设置显示等待
    def find_element(self,loc,method_loc=None,timeout=5):
        try:
            # 每隔0.5秒查找需要查找的元素，超时时间设置为5秒
            # WebDriverWait(self.driver,timeout,poll_frequency=0.5).until(lambda driver: driver.find_element(*loc))
            if method_loc == 'id':
                return self.driver.find_element_by_id(loc)
            elif method_loc == 'class_name':
                return self.driver.find_element_by_class_name(loc)
            elif method_loc == 'name':
                return self.driver.find_element_by_name(loc)
            elif method_loc == 'xpath':
                return self.driver.find_element_by_xpath(loc)
            else:
                return self.driver.find_element_by_android_uiautomator(loc)

        except:
            print("未找到元素")
    # 根据元素点击
    def click(self,loc):
        self.find_element(loc).click()
        # 每点击一个元素停留0.5秒
        time.sleep(0.5)

    # 根据坐标点击/触摸
    def tap_op(self,x,y,times=1000):
        self.driver.tap([(x,y)],times)


    def clear(self,loc):
        self.find_element(loc).clear()

    def send_keys(self,loc,value):
        # 先清除输入框
        self.clear(loc)
        self.find_element(loc).send_keys(value)

    # 系统按键如：返回、Home、菜单、搜索
    def key_event_back(self,value=4):
        """
        KEYCODE_BACK 返回键 4
        KEYCODE_HOME 按键Home 3
        KEYCODE_MENU 菜单键 82
        KEYCODE_ENTER 回车键 66
        KEYCODE_FORWARD_DEL 删除键 112
        KEYCODE_DEL 退格键 67
        KEYCODE_CAPS_LOCK 大写锁定键 115
        KEYCODE_ZOOM_IN 放大键 168
        KEYCODE_ZOOM_OUT 缩小键 169
        KEYCODE_SEARCH 搜索键 84
        KEYCODE_VOLUME_UP 音量增加键 24
        :param value:
        :return:
        """
        self.driver.keyevent(value)

    # 向上滑动
    def swipe_up(self,times=1000):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x*0.5,y*0.75,x*0.5,y*0.25,times)

    # 向下滑动
    def swipe_down(self,times=1000):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x*0.5,y*0.25,x*0.5,y*0.75,times)

    # 向左滑动
    def swipe_left(self, times=1000):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x*0.75, y*0.5, x*0.25, y*0.5, times)

    # 向右滑动
    def swipe_right(self,times=1000):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x*0.25,y*0.5,x*0.75,y*0.5,times)

    # 从元素a滑到元素b，用多久
    def scroll_page(self,ele_a,ele_b,times=2000):
        self.driver.scroll(ele_a,ele_b,times)


    # 长按操作
    def long_press(self,x1,y1,times=1000):
        TouchAction(self.driver).long_press(x1,y1).wait(times).release().perform()

    # 鼠标悬停
    def mouse_hover(self,loc,times=3):
        ActionChains(self.driver).move_to_element(loc).perform()
        time.sleep(times)

    # 判断元素是否存在
    def element_is_exits(self,loc):
        # 获取当前页面所有元素
        source = self.driver.page_source
        if loc in source:
            return True
        else:
            return "元素不存在"

    # 锁定屏幕
    def lock(self,times=5):
        self.driver.lock(times)

    # 将app放到后台
    def background_app(self,times=5):
        self.driver.background_app(times)

    # 关闭app
    def close_app(self):
        self.driver.close_app()

    # 收起键盘
    def close_keyboard(self):
        self.driver.hide_keyboard()

    # 重置app，相当于卸载重装
    def reset_app(self):
        self.driver.reset()

    # 打开通知栏
    def open_notifications(self):
        self.driver.open_notifications()

    # 截屏，并将图片保存在指定文件夹下
    def save_screenshot(self,img_name):
        self.driver.get_screenshot_as_file("../images/"+img_name)

