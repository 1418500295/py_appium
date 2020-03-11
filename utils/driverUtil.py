
from appium import webdriver
from utils.operate_yaml import ReadYaml

yaml_data = ReadYaml.get_yaml("app_config.yaml")


class DriverUtil():
    @staticmethod
    def get_driver():

        capabilities = {
            "platformName": yaml_data["platformName"],
            "deviceName": yaml_data["deviceName"],
            "app": r"C:\Users\ASUS" +"/" + yaml_data["app"]
        }

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)

        return driver

if __name__ == '__main__':
    print(DriverUtil.get_driver())

