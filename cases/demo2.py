from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
capabilities = {
    "platformName":"Android",
    "deviceName":"127.0.0.1:62001",
    "app":r"C:\Users\ASUS\Downloads\jinritoutiao_7640.apk",
    "noReset": "true"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
driver.implicitly_wait(5)

# driver.find_element_by_id("com.ss.android.article.news:id/aic").click()
# time.sleep(1)
# driver.find_element_by_id("com.ss.android.article.news:id/ae1").click()
driver.find_element_by_android_uiautomator('new UiSelector().textContains("总书记指挥这")').click()
driver.find_element_by_android_uiautomator('new UiSelector().description("赞")').click()
print(driver.contexts)