from appium import webdriver
import time

capabilities = {
    "platformName":"Android",
    "deviceName":"127.0.0.1:62001",
    "app":r"C:\Users\ASUS\chat_1.0.0.apk"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
driver.implicitly_wait(5)


driver.find_element_by_id("cn.guoguo.chat:id/edit_phone").send_keys("18849464646")
driver.find_element_by_id("cn.guoguo.chat:id/tv_login").click()
driver.find_element_by_id("cn.guoguo.chat:id/more").click()
loc_text = 'new UiSelector().text("发起群聊")'
driver.find_element_by_android_uiautomator(loc_text).click()
driver.find_element_by_android_uiautomator('new UiSelector().text("被哦哦婆")').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("播您明末地面MSN")').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("果果5149客厅哦里")').click()


driver.find_element_by_android_uiautomator('new UiSelector().text("确定(3)")').click()

driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.ImageButton")').click()

width = driver.get_window_size()["width"]
height =driver.get_window_size()["height"]

"""根据坐标点击"""
driver.tap([(180,887),(740,939)],500)

# eles = driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("cn.guoguo.chat:id/nameTextView")')
# for one in eles:
#     if "Daine哦" in one.text:
#         one.click()
#         break
driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.ImageButton")').click()
print(driver.contexts)
# driver.find_element_by_id("cn.guoguo.chat:id/iv_bottom_pour").click()


# 进入我的页面后设置退出app
# driver.find_element_by_android_uiautomator\
#     ('new UiSelector().resourceId("cn.guoguo.chat:id/me").className("android.widget.FrameLayout")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("设置")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("退出")').click()
#
# driver.find_element_by_id("cn.guoguo.chat:id/tv_ok").click()


"""
上滑
"""
# for i in range(5):
#
#     driver.swipe(start_x=180,start_y=1223,end_x=180,end_y=383,duration=2000)
#     time.sleep(0.5)
# print(width)


"""
左滑
"""
# for i in range(3):
#     driver.swipe(start_x=width*0.8,start_y=height*0.5,end_x=width*0.2,end_y=height*0.5)
#     time.sleep(0.5)
#
"""
右滑
"""
# for i in range(3):
#     driver.swipe(start_x=width*0.2,start_y=height*0.5,end_x=width*0.8,end_y=height*0.5)
#     time.sleep(0.5)







