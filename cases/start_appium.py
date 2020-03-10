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












